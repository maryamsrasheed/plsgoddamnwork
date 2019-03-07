"""
Unit 1, Assignment 1, Question 1

Conversion.py

A program to convert temperature degrees from Celsius to Fahrenheit and vice versa

By : Maryam Rasheed
Started : Mar 1/19
Modified : Mar 1/19
Finished :

"""

print("What type of conversion do you want?")
choice = input("Enter C for conversion from Celsius to Fahrenheit or enter F for conversion from Fahrenheit to Celsius: ")
if choice == "F" :
    temp_Fahrenheit = input("Enter the temperature degree in Fahrenheit: ")
    print(temp_Fahrenheit)
    temp_C = round((float(temp_Fahrenheit)- 32) * 5/9)
    print(temp_C)

elif choice == "C" :
    temp_Celsius = input("Enter the temperature degree in Celsius: ")
    print(temp_Celsius)
    temp_F = round(float(temp_Celsius) * 9/5 + 32)
    print(temp_F)


