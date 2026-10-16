
"""
def rav_String(s):
    if s=="":
        return ""
    return rav_String(s[1:])+s[0]

print(rav_String("hello"))
"""

# 2 

"""
def sum_playlist(durations):
    if durations==[]:
        return 0 
    return durations[0]+sum_playlist(durations[1:])

print(sum_playlist([120,180,200]))
"""

# 3  local and globle 

"""
count = 10 

def update_count():
    count = 5
    print("Inside:",count)
update_count()
print("Outside:",count)
"""

# 4 

"""
def count_likes(post):
    total = post["likes"]

    for reply in post.get("replies", []):
        total = total + count_likes(reply)

    return total


post = {
    "likes": 10,
    "replies": [
        {"likes": 5},
        {"likes": 3}
    ]
}

print(count_likes(post))

"""

# 5 

"""
app_status = "Offline"

def status():
    user_status = "Online"
    print("Inside:", user_status)

print("Before:", app_status)

status()

print("After:", app_status)
"""
