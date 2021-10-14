# 28 YEARS OF UFC HISTORY
EXTRACTION, PREPARATION, AND ANALYSIS OF THE ULTIMATE FIGHTING CHAMPIONSHIP HISTORICAL DATA

### Intro
With UFC’s (Ultimate fighting championship) rising popularity, I could not help but to dive into the dataset and see what interesting trends I could dig out. 

The main goal of this project is to perform a simple statistical analysis on UFC fighters and their attributes like weight, reach, career knockouts, etc. I will answer questions like: what fighter has the most knock outs? What is the standard deviation of a fighter’s height in each weight-division? How does height distribution look like in each weight-division? And other interesting questions. 

### DATA EXTRACTION
The data was downloaded from http://www.ufcstats.com using Python and a web-scraping library called [BeautifulSoup4](http://github.com).
The [Python script](https://github.com/estgarci/UFC-Data-Analysis/blob/main/data/extraction/extract_fighters.py) can be used to extract the present-day fighter roster.
The raw data contains every fighter from the year 1993 – present. 
### DATA PREPARATION
The data is missing a sex attribute; the UFC separates their fighting competitions by sex, so we must do the same with our dataset. 
### BUILDING THE SEX CLASSIFYER
Using historical registered names from www.datagov.org, I built a classifier that classifies a fighter's sex based on a fighter’s name. 
[code snippet]
The female’s feather weight-division is the only set of fighters that is already classified, as males do not have a feather weight-division. I used the female dataset to evaluate the precision and recall of the sex classifier.
[code snippet] 
The classifier has a 96% precision, a number that I consider 'good enough'. I could improve the classifier by feeding a machine learning model with fighter attributes such as name, weight, height, and reach. However, for the purposes of this project, 96% precision and 70% recall are good metrics to keep moving forward.
DATA ANALYSIS
