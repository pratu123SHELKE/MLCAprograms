
import pandas as pd

import numpy as np

from matplotlib import pyplot as plt

import seaborn as sns

#Step 1: loading dataset

print(df head(5))

df= pd.read_csv("D:/MLCALAB-Datafile/diabetes_dataset_expl.csv") #to print first 10 rows print("

#to print last 10 rows

print(df.tail(5))

#to print entire dataframe.

#print(df.to_string())

#Step 2: Check Data Structure and missing values

print("

Lab

#summary including count of non-null entries and data type of each column. df.info()

print(" print(df.isnull().sum()) -")

#Returns the number of missing values per column

print("---

#Step 3: show statistical summary and visualize outliers print(df.describe())

#Visualize spread and detect outliers using matplotlib's boxplot() fig, axs plt.subplots(len(df.columns), 1. figsize (7. 18), dpi-100) for i, col in enumerate(df.columns) axs[i] boxplot(df[col], orientation="horizontal")

axsi set ylabel(col)

plt.tight layout()

plt.subplots_adjust(hspace-1.0)

plt.show()

print("Remove Outliers

#Step 4. Remove Outliers Using the Interquartile Range (IQR) Method q1, q3=np percentile(df]'Glucose'], [25, 75]) iqr=q3-q1 lower=q1-1.5* igr upper q3+1.5* iqr clean_df = df[(df['Glucose'] >= lower) & (df['Glucose'] <= upper)] copy() print("Q1:", q1) print("Q3.", q3) print("IQR.", iqr) print("LOWER:", lower) print("UPPER:", upper) percentage = ((len(df) - len(clean_df)) / len(df)) * 100 print("Percentage of outliers removed", percentage)

print("Original shape:", df.shape) print("Cleaned shape.", clean_df.shape)

print("Correlation analysis--------------")