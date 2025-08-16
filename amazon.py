import pandas as pd
import kagglehub

# Download latest version
path = kagglehub.dataset_download("snap/amazon-fine-food-reviews")

df = pd.read_csv("./Reviews.csv")

# Initial exploration
print(df.describe())
print(df.info())
print(df.head(10))

# Removing or dropping columns
df = df.drop(['HelpfulnessNumerator', 'HelpfulnessDenominator'], axis = 1)

# Duplicates removal
df = df.drop_duplicates()

# Datatype Check
print(df.dtypes)
df['Time'] = pd.to_datetime(df['Time'], unit='s')

# Missing Values check
print(df.isnull().sum())
df = df.dropna(subset=['ProfileName', 'Summary'])

# Creating Sentiment of review
def get_sentiment(score):
    if score <= 2:
        return "Negative"
    elif score == 3:
        return "Neutral"
    else:
        return "Positive"

df['Sentiment'] = df['Score'].apply(get_sentiment)

# Reviews by sentiment
sentiment_counts = df['Sentiment'].value_counts()

# Reviews by product
product_stats = df.groupby('ProductId').agg(
    avg_rating=('Score', 'mean'),
    total_reviews=('Score', 'count'),
    positive_reviews=('Sentiment', lambda x: (x=='Positive').sum())
).reset_index()

# Reviews by time
df['YearMonth'] = df['Time'].dt.to_period('M')
time_trends = df.groupby(['YearMonth','Sentiment']).size().reset_index(name='count')

# Save cleaned dataset
df.to_csv("final_reviews.csv", index=False)