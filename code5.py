# Required Argument

def required_argument(name, roll_no):
    print("Required Argument:")
    print("Name:", name)
    print("Roll No:", roll_no)


# Keyword Argument

def keyword_argument(name, roll_no, div):
    print("\nKeyword Argument:")
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Division:", div)


# Default Argument

def default_argument(name, roll_no, div="A"):
    print("\nDefault Argument:")
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Division:", div)


# Variable Length Argument

def variable_length_argument(name, *subjects):
    print("\nVariable Length Argument:")
    print("Name:", name)
    print("Subjects:")
    for subject in subjects:
        print(subject)


# Taking input from user

name = input("Enter your name: ")
roll_no = input("Enter your roll number: ")
div = input("Enter your division: ")

subject1 = input("Enter subject 1: ")
subject2 = input("Enter subject 2: ")
subject3 = input("Enter subject 3: ")


# Function calls

required_argument(name, roll_no)

keyword_argument(name=name, roll_no=roll_no, div=div)

default_argument(name, roll_no)

variable_length_argument(name, subject1, subject2, subject3)