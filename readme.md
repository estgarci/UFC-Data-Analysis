# 28 YEARS OF UFC HISTORY
EXTRACTION, PREPARATION, AND ANALYSIS OF THE ULTIMATE FIGHTING CHAMPIONSHIP HISTORICAL DATA
### INTRO
The main goal of this project is to perform a simple statistical analysis on UFC fighters and their attributes like weight, reach, career knockouts, etc. I will answer questions like: what fighter has the most knock outs? What is the standard deviation of a fighter’s height in each weight-division? How does height distribution look like in each weight-division? And other interesting questions.

A detailed explanation of the analysis can be found in this project's [Python jupyter-notebook.](https://github.com/estgarci/UFC-Data-Analysis/blob/main/exploratory_analysis.ipynb)
### DATA EXTRACTION
I built a [web-scraping Python script](https://github.com/estgarci/UFC-Data-Analysis/blob/main/data/extraction/extract_fighters.py) that downloads public data from from www.ufcstats.com. The raw dataset contains a historical roster of fighters in the UFC; from the year 1993 to present.
### DATA PREPARATION
In order to analyze the dataset, raw data had to be stratified by gender and weight-division. However, the downloaded data did not contain either attributes by default. 

### BUILDING THE GENDER CLASSIFYER
To stratify the dataset by gender I built a [brute-force search algorithm using Python](https://github.com/estgarci/UFC-Data-Analysis/blob/main/name_sex_classifier/sex_classifier.py) that predicts fighters' gender given a fighter’s name. The algorithm uses historical names from the U.S national database www.datagov.org to predict the likelyhood that a name is traditionally male or female. The classifyer attained 96% precision and 70% recall, which was sufficient for the purposes of this project. I used the same technique to sort the roster by weight-division.

The females' feather weight-division is the only set of fighters that is already classified, as females do not have a feather weight-division. I used the female dataset to evaluate the precision and recall of the gender classifier. After running the classifier through the names in the feather weight-division, the classifier had 96% precision and 70% recall. I could improve the classifier by feeding a machine learning model with some fighter attributes such as name, weight, height, and reach. However, for the purposes of this project, 96% precision and 70% recall are good metrics to keep moving forward.
### DATA ANALYSIS

