"""
Week 2 - Data mining
By Christopher Diaz Montoya
"""
# Problem 1!!

store=[] # Empty array to store values
for a in range (1000, 2000): # Loop to check over all numbers in range
    if (a % 11 == 0) and not (a % 3 == 0):
# Above line makes sure if multiple of 11 and not of 3 execute line below
        store.append(str(a)) # Stores numbers that met above requirements
print (*store, sep = ", ")
# Learnt the above print line from the website below to print output correctly
# https://www.kite.com/python/answers/how-to-print-a-list-without-brackets-in-python#:~:text=Use%20*%20to%20print%20a%20list,set%20sep%20to%20%22%2C%20%22%20.

# Problem 2!!

print("Please input a sentance: ")  # Allows user to input sentance
sentance = input()
# Above line assigns input to the varibale called sentance
# Below 2 lines will be used as counters for upper and lower case letters
UpperCase = 0
LowerCase = 0
# For loop to check each character for the length of the string sentance
for char in range(len(sentance)):
# Below says if char is in the lower letter alphabet add  and assigns to lower
# case counter else if in the upper case alphabet add to the upper counter
    if(sentance[char]>='A' and sentance[char]<='Z'):
        UpperCase += 1
    elif(sentance[char]>='a' and sentance[char]<='z'):
# Learnt in my other module how to convert from lower case to upper case
# without libraries so played around with the code as it's like a range
# and that's how I got the above line
        LowerCase += 1 # Add 1 to counter
print('Upper case = ', UpperCase)
print('Lower case = ', LowerCase)
# Above prints the count and I used the comma to print the string and counter
# int. As I only mentioned the alpahbets there is no issue with the space and
# is not counted by accident.

# Problem 3!!

# Below made a funtion that turns an int into a string
def NumToWord(a):
    b = str(a) # Casts int into a string and stored in b
    print(b) # Prints b which is casted into a string
    print(type(b)) # Double check what daat tybe b is
# Below int is used to make sure input value is an integer, learnt last
# academic year.
num = int(input("Please enter a number: "))
NumToWord(num) # Calls functions and passes input "num" into the funciton.

# Problem 4!!

import itertools # Import from library to help iterate through all outcomes

# Below stored for easy access
subject = ["I", "You"]
verb = ["Read", "Borrow"]
ob = ["Shakerpeare's plays", "Shakespeare's poems"]

# Below prints and iterates over each possible out come from the lists 
# mentioned whille the varibles stay in the same order. List ensures prints
# in the right way
print(list(itertools.product(subject, verb, ob)))

# https://www.codegrepper.com/code-examples/python/how+to+find+all+combinations+of+a+list+python

# Problem 5!! Part 1

import matplotlib.pyplot as plt # imported and given a shorter name

x, y = [1, 2, 3], [2, 4, 1] # Assigning values to varibles x and y 
plt.xlabel("X axis", fontsize = 15) # Prints x label and size
plt.ylabel("Y axis", fontsize = 15) # Prints y label and size
plt.title("My first graph", fontsize = 20) # Prints title
# Learnt how to change size and label names from
# https://stackoverflow.com/questions/12444716/how-do-i-set-the-figure-title-and-axes-labels-font-size-in-matplotlib
# Some of above learnt from lectures and exra study help from uni.

# This plots the points on the graph
plt.plot(x, y)
plt.show() # This shows the graph

# Part 2

X = [] # Created empty lists to store values read from document
Y = []

a = open("test.txt", "r") # a is a variable which are the contents
for row in a: # Loops all rows in the txt file
    row = row.split(" ") # splits numbers in file when it reads a space
    X.append(row[0]) # First nunber is added to X 
    Y.append(int(row[1])) # Second number is added to Y

plt.xlabel("X axis", fontsize = 15) # Prints x label
plt.ylabel("Y axis", fontsize = 15) # Prints y label
plt.title("My second graph", fontsize = 20) # Prints title

plt.plot(X, Y) # This plots the points on the graph
plt.show() # This shows the graph

#https://www.geeksforgeeks.org/python-create-graph-from-text-file/

# Problem 6!!

# below importing relevant libraries
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv ("train.csv")
# Above imports and reads the data set

df.info() # Did this to see how many columns there are along with what data
# types are in the data set which are 3, along with being able to see which 
# columns have missing dat

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

