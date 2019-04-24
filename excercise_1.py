#Python3
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# import datetime to determine current year
import datetime
todays_date = datetime.datetime.now()
todays_year = todays_date.year

#ask user to enter their Name
user_name = input("What is your name? : ")
# ask for user age and convert into an interger 
user_age = int(input("Ok "+ user_name +", what is your age? "))

# year when user will turn 100 y/o
century_year = todays_year + (100 - user_age)
print(user_name +" Will be 100 years old on "+ str(century_year))
