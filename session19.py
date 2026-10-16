# 1,2

"""
class song:
    def __init__(self,title,artist,duration):
        self.title=title
        self.artist=artist
        self.duration=duration

s = song("Kesariya", "Arijit Singh", 268)

print(s.title)
print(s.artist)
print(s.duration)
"""

# 3 
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play_preview(self):
        print("playing 30sec preview of kesariya by arjit singh")


s = Song("Kesariya", "Arijit Singh", 268)

s.play_preview()

# 3 

class foodorder:
    rest_name=input("enter the restaurant name:")
    items=[]
    total_price=0

    for i in range(5):
        items=input("enter the items:")
        items.append(items)
        total_price +=int(input("enter the price:"))
    def show(self):
        print("restaurant")


# 4 


class FoodOrder:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.items = []
        self.total_price = 0

    def add_item(self, item, price):
        self.items.append(item)
        self.total_price += price


# Create object
order = FoodOrder("Pizza Hut")

# Add two items
order.add_item("Pizza", 250)
order.add_item("Burger", 120)

# Print details
print("Restaurant:", order.restaurant_name)
print("Items:", order.items)
print("Total Price:", order.total_price)


# 5 


class Song:
    def __init__(self, name):
        self.name = name
        self.play_count = 0

    def increment_play_count(self):
        self.play_count += 1


# Create object
song = Song("Kesariya")

# Play song 3 times
song.increment_play_count()
song.increment_play_count()
song.increment_play_count()

# Print details
print("Song:", song.name)
print("Play Count:", song.play_count)

