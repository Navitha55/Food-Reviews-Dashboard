# 🍽️ Amazon Food Reviews Sentiment Dashboard
This project analyzes 568K+ Amazon food product reviews to uncover customer sentiment patterns using Natural Language Processing (NLP) and presents the insights in an interactive Power BI dashboard.
The analysis provides an end-to-end workflow starting from data cleaning & preprocessing (Python) to sentiment classification (NLP) and finally data visualization (Power BI).

## 🎯 Objectives
- Perform data cleaning & preprocessing (handle missing values, datatype conversions).
- Generate a sentiment column (Positive / Negative / Neutral) using NLP techniques.
- Build an interactive Power BI dashboard to visualize customer opinions.
- Enable businesses to understand customer satisfaction, product trends, and review patterns.

## 🗂 Dataset
- Source: Amazon Fine Food Reviews Dataset (Kaggle)
- You can download from python script

## ⚙️ Data Preprocessing (Python)
- Handled Null Values in ProfileName and Summary.
- Converted UNIX Time → Date format (Year, Month, Quarter extracted).
- Applied NLP Preprocessing:
- Lowercasing, punctuation removal, tokenization.
- Sentiment classification using TextBlob / VADER.
- Created Sentiment Column with 3 classes:
- Positive (Score ≥ 4)
- Neutral (Score = 3)
- Negative (Score ≤ 2)
- 👉 Python cleaning script is available in the repository.

## 📊 Power BI Dashboard Features
- KPI Cards: Total Reviews, Positive, Negative, Neutral.
- Sentiment Distribution: Pie/Donut chart for % share.
- Trend Analysis: Monthly & Yearly review counts with sentiment breakdown.
- Top Reviewers: Identifying most active reviewers.
- Quarterly Analysis: Seasonality in review patterns.
- Interactive Filters: Year, Sentiment, Product selection.

 ## 🔍 Key Insights
- ✅ Majority (~85–90%) of food reviews are positive.
- ⚠️ Negative reviews, though fewer, often highlight issues with product quality & packaging.
- 📈 Review volume peaked in certain months, suggesting seasonal demand trends.
- 🏆 A small group of reviewers contributes a large portion of reviews.

 ## 🚀 How to Run
- Download dataset from Kaggle.
- Run the Python preprocessing script → generates cleaned dataset with sentiment column.
- Load the cleaned dataset into Power BI.
- [Download PBIX File](https://drive.google.com/file/d/1pu2ws05kF7pcMEPTSDtfk-kHUgRjd7nM/view?usp=sharing)

##  📌 Tools & Technologies
- Python: Pandas, NumPy, NLTK/TextBlob, Matplotlib/Seaborn
- Power BI: Dashboard development & interactive visualizations
- Dataset Source: Kaggle (Amazon Fine Food Reviews)

## 🏆 Outcome
This project demonstrates an end-to-end NLP + Business Intelligence pipeline, bridging the gap between text analytics and business insights.It strengthens real-world data analytics skills by combining data preprocessing, NLP sentiment analysis, and BI dashboarding in one project.

<img width="1267" height="705" alt="Amazon" src="https://github.com/user-attachments/assets/088c1b55-0a91-413b-a2ec-847fa6d203ca" />

## Contributions 
- Feel free to fork, improve, add features or difficulty levels, and submit pull requests!

## License
- This project is open source and available under the MIT License.
