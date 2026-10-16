# 1 
movies = ["Pushpa 2", "Stree 2", "Jawan", "Animal", "Leo"]

movie_iter = iter(movies)

print(next(movie_iter))
print(next(movie_iter))
print(next(movie_iter))
print(next(movie_iter))
print(next(movie_iter))

# 2 

songs = ["Kesariya", "Tum Hi Ho", "Apna Bana Le", "Chaleya", "Heeriye", "Satranga"]

for position, song in enumerate(songs, 1):
    print(position, ".", song)

# 3 

foods = ["Pizza", "Burger", "Sandwich", "Pasta"]
prices = [250, 150, 120, 200]

for food, price in zip(foods, prices):
    print(food, "-", "₹", price)

# 4 
def insta_posts_generator(posts):
    for post in posts:
        yield post


posts = ["Good Morning!", "New Photo!", "Weekend Vibes", "Travel Time"]

post_generator = insta_posts_generator(posts)

try:
    while True:
        print(next(post_generator))
except StopIteration:
    print("All posts printed.")

# 5 

def cashback_generator(transactions):
    for amount in transactions:
        yield amount * 0.05


transactions = [100, 500, 1000, 2000]

cashback = cashback_generator(transactions)

for value in cashback:
    print("Cashback:", value)


