"""
Week 3 - Data mining
By Christopher Diaz Montoya
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")
print("Amount of rows = {}\nAmount of colu\
mns = {}".format(df.shape[0], df.shape[1]))
# Above row is to see the shape of the data set
print(df.head)
# Above row is to print table of data set to see what it lokks like

df.info()

# Drops/gets rid of the ID column as it is not needed
df = df.drop(columns = ["Loan_ID"])

columns = df.columns.tolist() # Everything in data frame
for x in columns:
  print("Missing data in {} : {}".format(x, df[x].isnull().sum()))
# Checks over column and then rows, the first {} represents column names
# the second {} represents amount of missing data.

# Turning loan status into 0 or 1
l1 = LabelEncoder() # Label encoder used from sklearn to normalize data 
# to give it a value between 0 and 1
l1.fit(df["Loan_Status"]) # This is the column that is normailized
df.Loan_Status = l1.transform(df.Loan_Status) # The column is updated on the
# whole data frame, each is repeated for each categorical data type.

# Turning gender status into 0 or 1
l1 = LabelEncoder()
l1.fit(df["Gender"])
df.Gender = l1.transform(df.Gender)

# Turning married status into 0 or 1
l1 = LabelEncoder()
l1.fit(df["Married"])
df.Married = l1.transform(df.Married)

# Getting rid of + to just numbers can be read easier
l1 = LabelEncoder()
l1.fit(df["Dependents"])
df.Dependents = l1.transform(df.Dependents)

# Turning employed and self emplyed to 0 and 1 easier to work with
l1 = LabelEncoder()
l1.fit(df["Self_Employed"])
df.Self_Employed = l1.transform(df.Self_Employed)

# Turning graduate and non graduate in eduaction to 0 and 1
l1 = LabelEncoder()
l1.fit(df["Education"])
df.Education = l1.transform(df.Education)

# Sets property location to a numerical value based on the 3 lcoations
l1 = LabelEncoder()
l1.fit(df["Property_Area"])
df.Property_Area = l1.transform(df.Property_Area)
print(df) # Prints out data frame to check all values are of numerical type 
# Above is data transformation

df.fillna(df.median(), inplace = True) # Fills in missing values with median
allColumns = df.columns # allColumns = all columns in the data frame
for col in allColumns: #For each column
  df[col] = pd.to_numeric(df[col]) # Turns argument into a numeric type
  
  
# Below is same code as above to check for missing data   
columns = df.columns.tolist()
for x in columns:
  print("Missing data in {} : {}".format(x, df[x].isnull().sum()))
# Above isnull().sum() was used to check missing values, learnt in class

df["Loan_Status"].value_counts(normalize=True).plot.bar() 
# Used to see the column which shows how many people got approved in a barchart

catColumns = ["Gender", "Married", "Dependents", "Education", "Self_\
Employed", "Property_Area", "Credit_History"]
for x in catColumns: # Loops over all data in each column
# Crosstab checks against another group of data I want to analyse against,
# in this case Loan_Status https://pbpython.com/pandas-crosstab.html against 
# all the columns in Columns
    y = pd.crosstab(df["Loan_Status"], df[x], normalize = "columns")
# https://www.journaldev.com/45109/normalize-data-in-python taught me how
# to normalize data and https://machinelearningmastery.com/rescaling-data-for-machine-learning-in-python-with-scikit-learn/#:~:text=Normalization%20refers%20to%20rescaling%20real,preparation%20of%20coefficients%20in%20regression.
# taught me what it does, makes all values inbetween 0 and 1.
    print(y) # Prints output
    y.plot(kind = "bar") # Plots bar chart for each column

df.boxplot(column = "ApplicantIncome", by = "Education") # Wanted to see the 
# correlation between graduate income and non graduate income

numColumns = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term"]

# I did above as I wanted to check if graduates earned more than non graduates
# Learnt this in lectue slides
for z in numColumns: # For loop to make a graph for each column
    # for each loop until every column in numColumns has a graph
    # shows column in numColumns against Loan_status
    result = df.boxplot(column = z, by = "Loan_Status") # Plots graph
    plt.show(result) # Shows graphs
# The graphs used in the abov loop were learnt from the lecture slides

df.info()