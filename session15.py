
# 1 
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


print(safe_divide(10, 2))
print(safe_divide(10, 0))

# 2 
try:
    reviews = int(input("Enter number of reviews: "))
    stars = int(input("Enter total stars: "))

    rating = stars / reviews
    print("Average rating:", rating)

except ValueError:
    print("Error: Please enter numbers only.")


# 3 
class InvalidDurationError(Exception):
    pass


def get_playlist_duration(songs):
    total = 0

    for duration in songs:
        if duration < 0:
            raise InvalidDurationError("Duration cannot be negative")
        total += duration

    return total / 60


songs = [180, 240, 300]

try:
    print("Total duration:", get_playlist_duration(songs), "minutes")
except InvalidDurationError as e:
    print("Error:", e)


# 4 

try:
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

except ValueError:
    print("Invalid input!")

else:
    total = price * quantity
    print("Total price:", total)

finally:
    print("Thank you for shopping!")



# 5 
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Error: Please enter numbers only.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    