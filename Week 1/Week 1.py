"""
Week 1 - Data mining
By Christopher Diaz Montoya
"""
# Problem 1!!

# Here I used varibles to store the values, then added both variables.

num1 = 52
num2 = 78
print("The result is", num1 + num2) 
# num1 + num2 is in brackets so this is figured out first before printing.
# "," was learnt last academic year in uni to display it on 1 line.

# Problem 2!!

""" Here I just multiplied the output by 4. Learnt in first year.
 If you multiply a string by x it prints out the same string  
 x amount of times. """

print("Hello, world! " * 4)

# Problem 3!!

"""Here I used \ for a new line in the string (code), \n for a new line in
the output and \t for tabs, creates 4 spacebars in the output. All learnt
last academic year along with being recapping during this weeks lecture."""

print("Twinkle, twinkle, little star, \n \t \tHow I wonder\
 what you are! \n \t \t \t Up above the world so high, \n \
 \n \t \t \t Like \a diamond in the sky. \n Twinkle twinkle,\
 little star, \n \t \t How I wonder what you are.")

# Challenge 1!!

"""Here I used the inbuilt input function for the computer to read my input
I assigned it to a variable called word. The input functions only reads 
it as a string for input unless specified, but only using a string for this."""

word = input("Enter a word: ")

# Here I converted the word to a list learnt in first year of uni.
# Recapped on https://www.w3schools.com/python/ref_func_list.asp

letters = list(word) # Converts inputted word into a list

"""Below is storing the even and odd index char
Here I used list slicing to help get every even indexed char"""

store_even = letters[::2] 
"""Starts from index 0, then stores every second char
until the end of the string. Recapped list slicing with below.
https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing"""
 
print("The charecters present at an even index are:", *store_even, sep=" - ")

"""Above used "," to print out more then one thing on the same line together 
and called the store_even variable for even indexed numbers. Learnt how to 
print lists without [] in week 2 from
https://www.kite.com/python/answers/how-to-print-a-list-without-brackets-in-python#:~:text=Use%20*%20to%20print%20a%20list,set%20sep%20to%20%22%2C%20%22%20.
so I added it week 1"""

# Challenge 2!!

"""Here I was asked to do the challenge with a funciton,
learnt functions in python in semester 1 last academic year."""

def pattern():
    num=0 # Created a variable and assigned it 0.
    while num < 5: # While loop learnt least year, meaning code after it
# will keep running while num is less than 5 and stop when num = 5.
        num += 1 # Adds and assigns 1 to num, so each time it loops it adds
        # 1 to num.
        converted_num = str(num) # Casting num to a string so multiple of 
# the same number appear when multiplied, if it is not converted to a string it 
# would print out an integer so 2*2 would print 4 instead of 22.
        print(converted_num * num) # Multiply string by int, both technically 
# the same number but the data type makes a huge difference.

pattern() 
"""Calls function and runs the code inside
https://stackoverflow.com/questions/17778372/why-does-my-recursive-function"""