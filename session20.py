
class product:
    def __init__(self,price):
        self._price=price

    def display(self):
        print(self._price)

p=product(500)
p.display()


# 2   get and set 

class product:
    def __init__(self,price):
        self._price=price

    def get_price(self):
        return self._price

    def set_price(Self,price):
        if price<0:
            print

# 3 


class Playlist:
    def __init__(self):
        self._songs = []

    def add_song(self, song):
        self._songs.append(song)

    def remove_song(self, song):
        if song in self._songs:
            self._songs.remove(song)

    def get_songs(self):
        return self._songs


p = Playlist()
p.add_song("Kesariya")
p.add_song("Apna Bana Le")

print(p.get_songs())

p.remove_song("Kesariya")
print(p.get_songs())


# 4 


from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UPI(PaymentMethod):
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


p1 = UPI()
p1.pay(500)

p2 = CreditCard()
p2.pay(1000)



