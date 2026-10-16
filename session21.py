# 1 


class Product:
    def get_discount(self):
        return 0

class Electronics(Product):
    def get_discount(self):
        return 10

p = Product()
e = Electronics()

print(p.get_discount())
print(e.get_discount())


# 2 


class FoodOrder:
    def calculate_total(self):
        return 500

class ZomatoOrder(FoodOrder):
    def calculate_total(self):
        return 500 + (500 * 5 / 100)

f = FoodOrder()
z = ZomatoOrder()

print(f.calculate_total())
print(z.calculate_total())


# 3 


class Influencer:
    def bonus(self):
        return 2000

class BrandManager:
    def bonus(self):
        return 5000

def show_bonus(employee):
    print(employee.bonus())

i = Influencer()
b = BrandManager()

show_bonus(i)
show_bonus(b)


# 4


class User:
    def get_status(self):
        return "active"

class PremiumUser(User):
    def get_status(self):
        return "premium"

u = User()
p = PremiumUser()

print(u.get_status())
print(p.get_status())

