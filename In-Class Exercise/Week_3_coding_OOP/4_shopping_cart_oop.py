# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_items(self, item, price):
#         self.items.append((item, price))
#         print(f"{item} added to cart and it's price is {price}.")

#     def remove_item(self, item, price):
#         for i in range(len(self.items)):
#             name, p = self.items[i]
#             if name == item and p == price:
#                 self.items.pop(i)
#                 print(f"{item} removed from cart.")
#                 return
#         print("item not found!")

#     def show_cart(self):
#         print("Cart items:")
#         for product in self.items:
#             print(product)

# cart1 = ShoppingCart()
# cart1.add_items("Apple", 10)
# cart1.add_items("Banana", 5)
# cart1.show_cart()
# # cart1.remove_item('Apple', 10)

# Exercise 4: Linrary
# attributes books
# methods 
# add_books(title, price)
# remove_book(title, price)
# total_price() -> 15
# show_books()

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, price):
        self.books.append((title, price))
        print(f"{title} added to library and price is ${price}.")

    def remove_book(self, title):
        for book in self.books:
            if book[0] == title:
                self.books.remove(book)
                print(f"{title} removed")
                return
        print("Book not found")

    def total_price(self):
        total = 0
        for book in self.books:
            total += book[1]
        return total
    
    def show_books(self):
        print("Books are:")
        for book in self.books:
            print(book)


library1 = Library()
library1.add_book("Python", 10)
library1.add_book("DSA", 15)
library1.show_books()
print(library1.total_price())