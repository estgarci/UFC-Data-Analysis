# 28 Years of UFC History
Extraction, preparation, and analysis of the ultimate fighting championship historical data.

### Purpose
The purpose of this project was to use python for data mining and analysis. The main objective was to perform an exploratory analysis on a historical data-set.

### Central questions
#####   1. What's the standard deviation of a fighter’s height in each weight division?
#####   2. How does height distribution look like in each weight division? 

### Data extraction
I built a [web-scraping Python script](https://github.com/estgarci/UFC-Data-Analysis/blob/main/data/extraction/extract_fighters.py) that downloads public data from www.ufcstats.com. The raw dataset contains a historical roster of fighters in the UFC. It contains data from the year 1993 to present.

### Data preparation
The raw data does not contain a division attribute by default. A classifyer was built to predict the missing value of a fighter based on their name.

I built an [algorithm using Python](https://github.com/estgarci/UFC-Data-Analysis/blob/main/name_sex_classifier/sex_classifier.py) that predicts fighters gender based on their name. The algorithm uses historical names from the U.S national database www.datagov.org to determine if a fighter belongs to the female or male division based on the relative proportion of males/females. The classifyer attained 96% precision and 70% recall.

### Data Analysis
A detailed explanation of the analysis can be found in this project's [Python jupyter-notebook.](https://github.com/estgarci/UFC-Data-Analysis/blob/main/exploratory_analysis.ipynb)

