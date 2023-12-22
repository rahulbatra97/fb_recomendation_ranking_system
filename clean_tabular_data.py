#In this file, you will write code to clean the tabular dataset.
#Handling missing data is an important step in data cleaning, as it can significantly impact the results of your analysis. 
#Missing data can lead to biased estimates, reduce the statistical power of your analysis, and ultimately lead to invalid conclusions.
#Here are the data cleaning steps you need to perform:
#You need to first remove all the null values in any column.


#loading the dataset
import pandas as pd
dataset = pd.read_csv("Products.csv")


#removing null values and removing unwanted characters (£)
df = dataset.dropna(0,thresh = 5)
df['price'] = df['price'].replace({r'£': '', r',': '', r'\)': '', r'-': '', r' ': ''}, regex=True)
print(df.info)




