# ==========================================
# Experiment 1: Types of Arguments in Python
# Name: ujjwal chavan
# Roll No:
# Division:
# ==========================================

# -------------------------------
# 1. Required Argument
# -------------------------------
def student(roll_no, name):
    print("Required Argument")
    print("Roll Number:", roll_no)
    print("Name:", name)

student(1, "ujjwal")


print("\n-------------------------------")

# -------------------------------
# 2. Keyword Argument
# -------------------------------
def student(roll_no, name):
    print("Keyword Argument")
    print("Roll Number:", roll_no)
    print("Name:", name)

student(name="ujjwal", roll_no=61)


print("\n-------------------------------")

# -------------------------------
# 3. Default Argument
# -------------------------------
def student(roll_no, name, division="A"):
    print("Default Argument")
    print("Roll Number:", roll_no)
    print("Name:", name)
    print("Division:", division)

student(1, "ujjwal")


print("\n-------------------------------")

# -------------------------------
# 4. Variable-Length Argument
# -------------------------------
def student(name, *subjects):
    print("Variable-Length Argument")
    print("Name:", name)
    print("Subjects:")
    for subject in subjects:
        print(subject)

student("ujjwal", "Python", "Java", "HTML", "CSS")