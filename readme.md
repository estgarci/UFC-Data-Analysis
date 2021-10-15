# 28 YEARS OF UFC HISTORY
EXTRACTION, PREPARATION, AND ANALYSIS OF THE ULTIMATE FIGHTING CHAMPIONSHIP HISTORICAL DATA
### INTRO
With UFC’s (Ultimate fighting championship) rising popularity, I could not help but to dive into the dataset and see what interesting trends I could discover. 

The main goal of this project is to perform a simple statistical analysis on UFC fighters and their attributes like weight, reach, career knockouts, etc. I will answer questions like: what fighter has the most knock outs? What is the standard deviation of a fighter’s height in each weight-division? How does height distribution look like in each weight-division? And other interesting questions.

A detailed explanation of the analysis can be found in [this project's notebook](https://github.com/estgarci/UFC-Data-Analysis/blob/main/exploratory_analysis.ipynb)
### DATA EXTRACTION
The data was downloaded from http://www.ufcstats.com using Python and a web-scraping library called [BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/).

The [Python script extracts raw data](https://github.com/estgarci/UFC-Data-Analysis/blob/main/data/extraction/extract_fighters.py) into a .json object that contains every fighter in the UFC, from the year 1993 to present.
### DATA PREPARATION
The obvious way to sort the raw data is by following the UFC guidelines. That is; sort the data by sex, and then sort each sex into their current weight division. Unfortunately, the raw data does not contain either a weight-division or sex attribute. The raw data needed to be stratified before it was analyzed. Sorting the raw data by weight-division was trivial, however, sorting by sex required a sex-classifyer.

### BUILDING THE SEX CLASSIFYER
I wrote a [Python script that classifies a fighter's sex](https://github.com/estgarci/UFC-Data-Analysis/blob/main/name_sex_classifier/sex_classifier.py) based on a fighter’s name. It uses the historical registered names from www.datagov.org to classify a name as male or female.

The female’s feather weight-division is the only set of fighters that is already classified, as males do not have a feather weight-division. I used the female dataset to evaluate the precision and recall of the sex classifier.

After running the classifier through the feather weight-division, the classifier had 96% precision and 70% recall. I could improve the classifier by feeding a machine learning model with fighter attributes such as name, weight, height, and reach. However, for the purposes of this project, 96% precision and 70% recall are good metrics to keep moving forward.
### DATA ANALYSIS

