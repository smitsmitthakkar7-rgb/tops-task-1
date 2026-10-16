
# 1 lambda 

"""
gst = lambda price : price + (price*18/100)

print(gst(100))
print(gst(250))
print(gst(500))
"""

# 2 

"""
songs = [' shape OF you ', ' perfect ', '  believer']
result = list(map(lambda x: x.strip().title(),songs))

print(result)
"""

# 3 start with s  

"""
products = ['Samsung', 'Apple', 'Shoes', 'Laptop', 'Speaker']
result = list(filter(lambda x: x.lower().startswith('s'),products))

print(result)
"""

# 4 

from functools import reduce

orders = [120,340,560,80]
total = reduce(lambda a,b :a+b,orders)

print(total)

# 5 map filter reduce 

from functools import reduce

numbers = [40,60,80,120]

double = map(lambda x:x*2,numbers)

greater = filter(lambda x:x>100,double)

total = reduce(lambda a,b:a+b,greater)

print(total)
