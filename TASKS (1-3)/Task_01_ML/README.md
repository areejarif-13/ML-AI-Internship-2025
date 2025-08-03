 **ML-AI-Internship-2025
Tasks provided for DevelopersHub.**
# **Task 1:**
## **Exploring and Visualizing a Simple Dataset**
### **Objective:**
Learn how to load, inspect, and visualize a dataset to understand data trends and distributions.
Dataset:
Iris Dataset (CSV format, can be loaded via seaborn or downloaded) Instructions:
● Load the dataset using pandas.
● Print the shape, column names, and the first few rows using .head().
● Use .info() and .describe() for summary statistics.
● Visualize the dataset:
○ Create a scatter plot to show relationships between features.
○ Use histograms to show value distributions.
○ Use box plots to identify outliers.
● Use matplotlib and seaborn for plotting.
### **Skills:**
● Data loading and inspection using pandas
● Descriptive statistics and data exploration
● Basic plotting and visualization with seaborn and matplotlib
# **=======FINDINGS=========****

### **=======Shape=======**
(103, 14)

### =======Columns Name=======

Index(['Brand', 'Model', 'AccelSec', 'TopSpeed_KmH', 'Range_Km',
       'Efficiency_WhKm', 'FastCharge_KmH', 'RapidCharge', 'PowerTrain',
       'PlugType', 'BodyStyle', 'Segment', 'Seats', 'PriceEuro'])
### ======Rows & Columns & Count=====
Rows= 5
Columns= 14
Count= 103


### =======Describe=======
	         AccelSec  TopSpeed_KmH  ...       Seats      PriceEuro
count  103.000000    103.000000  ...  103.000000     103.000000
mean     7.396117    179.194175  ...    4.883495   55811.563107
std      3.017430     43.573030  ...    0.795834   34134.665280
min      2.100000    123.000000  ...    2.000000   20129.000000
25%      5.100000    150.000000  ...    5.000000   34429.500000
50%      7.300000    160.000000  ...    5.000000   45000.000000
75%      9.000000    200.000000  ...    5.000000   65000.000000
max     22.400000    410.000000  ...    7.000000  215000.000000
	
* count	Number of non-null (non-empty) values in the column.	
* mean	The average value of the column.	
* std	Standard deviation — measures spread/variability in data.	
* min	The minimum (smallest) value in the column.	
* 25%	1st quartile (Q1) — 25% of the data lies below this value.	
* 50%	Median (Q2) — middle value; 50% of data lies below this.	
* 75%	3rd quartile (Q3) — 75% of the data lies below this value.	
* max	The maximum (largest) value in the column.

### Overview
This overview helps us to identify the statistical values of the data considered.