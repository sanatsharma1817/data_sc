# QUESTION 5 IS HERE 

# Take a dataset  from google , specifically works with shopping data . 
# Like swiggy and Zomato . Work on data cleaning , replace
# the data with averages if the data column is about amount and number of
# models replace the null cells of remaining with null cells .


import pandas as pd
import numpy as np

# load dataset
df = pd.read_csv("numpy_practice_dataset.csv")

print("\noriginal dataset")
print(df.head())

# checking null values
print("\nnull values before cleaning")
print(df.isnull().sum())

# data cleaning
for column in df.columns:

    # if column datatype is number
    if df[column].dtype == "int64" or df[column].dtype == "float64":

        # fill null with average
        avg = df[column].mean()
        df[column].fillna(avg, inplace=True)

    else:
        # fill remaining null values with "null"
        df[column].fillna("null", inplace=True)

print("\nnull values after cleaning")
print(df.isnull().sum())

# save cleaned dataset
df.to_csv("cleaned_practice.csv", index=False)

print("\ndataset cleaned successfully")
print("new file created : cleaned_practice.csv")
