
# 1 

"""
file = open("my_playlist.txt","w")

file.write ("shape of you\n")
file.write ("my name is smit\n")
file.write ("fav game is cricket\n")
file.write ("fav food is panipuri\n")

file.close()
"""

# 2 

"""
file = open("my_playlist.txt","r")

for song in file:
    print(song.strip().upper())

file.close()
"""

# 3   file read..

"""
import csv

file = open("ipl.csv", "r")

data = csv.DictReader(file)

for row in data:
    print(row["Winner"])

file.close()
"""

# 5 
from pathlib import Path

file = Path("zomato_orders.json")

if file.exists():
    print("File found")
else:
    print("File not found")