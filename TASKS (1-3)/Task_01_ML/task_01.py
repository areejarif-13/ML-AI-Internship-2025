#--------------------------------------------ML/AI_Internship_2025_TASK_01
#-----------------------------------import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontEntry
#---------- Function for Scatter Plot --------------
def function_scatter_plot(X,Y,feature,name_value_x,name_value_y):
    sns.scatterplot(data=df, x=X, y=Y, color=feature,hue='Segment' , style='BodyStyle',size='Seats')
    plt.title(f"Scatter Plot between {name_value_x} vs {name_value_y}")
    plt.xlabel(X)
    plt.ylabel(Y)
    plt.grid(True)
    plt.legend(loc="best")
    plt.xticks(rotation=45,size=5)
    plt.yticks(rotation=0,size=5)
    plt.tight_layout()
    plt.show()
#---------- Function for Histogram --------------
def function_histogram_plot(X,color,Title):
    df[X].hist(bins=30, color=color, histtype='bar', edgecolor='black')
    plt.title(f"Histogram of {Title}")
    plt.xlabel(f"{X}")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45, size=8)
    plt.yticks(rotation=0, size=8)
    plt.tight_layout()
    plt.show()
#---------- Function for Box Plot --------------
def function_box_plot(Y,X,Color,Title):
    sns.boxplot(data=df, x=X,y=Y, color=Color)
    plt.title(f"Boxplot of {Title}")
    plt.xlabel(f"{X}")
    plt.ylabel(f"{Y}")
    plt.xticks(rotation=45, size=10)
    plt.yticks(rotation=0, size=10)
    plt.tight_layout()
    plt.show()
#---------- Function for printing --------------
def printing(prompt,name):
    print(f"======={name}=======")
    print(f"\t{prompt}")
    print("====================")
#-------------------------------------------------------------functions
#----------------------------Load the dataset using pandas.
df = pd.read_csv("ElectricCarData_Clean.csv")
#----------------------------Print the shape, column names, and the first few rows using .head().
printing(df.shape,"Shape")
printing(df.columns,"Columns")
printing(df.head(),"Head")
printing(df.count(),"Count")

#----------------------------Use .info() and .describe() for summary statistics.
print("=======Information=======")
df.info()
print("=========================")
printing(df.describe(),"Describe")
#-----------------------------Visualize the dataset:
# ----------------------------Use matplotlib and seaborn for plotting.
#----------------------------------------------------SCATTER_PLOT
#What is the relationship between AccelSec (acceleration) and TopSpeed_KmH?
function_scatter_plot("AccelSec","TopSpeed_KmH",'red',"Acceleration per sec","Top Speed km/h")
# Does Range_Km increase with Efficiency_WhKm or FastCharge_KmH?
function_scatter_plot("Range_Km","Efficiency_WhKm",'pink',"Range per Km","Efficiency km/h")
function_scatter_plot("Range_Km","FastCharge_KmH",'purple',"Range per Km","Fast Charge km/hr")
# Is there a visible trend between PriceEuro and TopSpeed_KmH?
function_scatter_plot("PriceEuro","TopSpeed_KmH",'green',"Price per Euro","Top Speed km/hr")
# Does PriceEuro correlate with Range_Km?
function_scatter_plot("PriceEuro","Range_Km",'orange',"Price per Euro","Range per Km")
# Is there any pattern between AccelSec and PriceEuro?
function_scatter_plot("AccelSec","PriceEuro",'yellow',"Acceleration per sec","Price per Euro")
# How does Efficiency_WhKm relate to AccelSec?
function_scatter_plot("Efficiency_WhKm","AccelSec",'grey',"Efficiency km/h","Acceleration per sec")
# # Brand', 'Model', 'AccelSec', 'TopSpeed_KmH', 'Range_Km',
# # 'Efficiency_WhKm', 'FastCharge_KmH', 'RapidCharge', 'PowerTrain',
# # 'PlugType', 'BodyStyle', 'Segment', 'Seats', 'PriceEuro'"""
#------------------------------------------------HISTOGRAM
# What is the distribution of PriceEuro across all cars?
function_histogram_plot("PriceEuro",'grey',"distribution of PriceEuro across all cars")
# How are values of TopSpeed_KmH distributed?
function_histogram_plot("TopSpeed_KmH",'red',"distribution of Top Speed of the cars (km/h)")
# What is the most common range (Range_Km) of electric vehicles?
function_histogram_plot("Range_Km",'orange',"distribution of Range_km across all cars")
# Is there a skew in FastCharge_KmH among the vehicles?
function_histogram_plot("FastCharge_KmH",'blue',"distribution of FasrCharge_km across all cars")
# How are Seats distributed across the dataset?
function_histogram_plot("Seats",'cyan',"distribution of Seats across all cars")
# What is the spread of AccelSec (acceleration times)?
function_histogram_plot("AccelSec",'brown',"spread of AccelSec (acceleration times)")
#------------------------------------------------BOX_PLOT
# Are there outliers in PriceEuro across different Segments?
function_box_plot("PriceEuro","Segment",'cyan',"Price per Euro with diffrent Segmnets")
# How does TopSpeed_KmH vary across PowerTrain types?
function_box_plot("TopSpeed_KmH","PowerTrain",'skyblue',"Price per Euro with Power Train")
# Which BodyStyle has the widest variation in Range_Km?
function_box_plot("BodyStyle","Range_Km",'grey',"Body Style with Range (km)")
# Is Efficiency_WhKm significantly different across PlugType?
function_box_plot("Efficiency_WhKm","PlugType",'purple',"Efficiency (Whkm) with Plug Type")
# Do Seats vary widely across different BodyStyle categories?
function_box_plot("Seats","BodyStyle",'pink',"Seats variation with Body Style")
# Are there pricing outliers (PriceEuro) in different PowerTrain types?
function_box_plot("PriceEuro","PowerTrain",'cyellow',"Price per Euro with Power Train Styles")