# 1 

import math

num = 25

print("Square root:", math.sqrt(num))
print("Factorial:", math.factorial(num))
print("Value of pi:", math.pi)

# 2 

import os

files = os.listdir()

for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        print(file)

# 3 

from datetime import datetime

date = input("Enter date (YYYY-MM-DD): ")

date = datetime.strptime(date, "%Y-%m-%d")

print("Day:", date.strftime("%A"))

# 4 

def format_follower_count(n):
    if n >= 1000000:
        return str(round(n / 1000000, 1)) + "M"
    elif n >= 1000:
        return str(round(n / 1000, 1)) + "K"
    else:
        return str(n)


