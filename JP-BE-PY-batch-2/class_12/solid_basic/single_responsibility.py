"""
S - Single Responsibility Principle (SRP):

A class should have only one reason to change, meaning it should have only one job or responsibility. 
This principle promotes the separation of concerns, making the system easier to understand and modify.
"""
# before
class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, price):
        book = {'id': len(self.books) + 1, 'title': title, 'author': author, 'price': price}
        self.books.append(book)

    def get_books(self):
        return self.books

    def process_order(self, book_id, customer_name):
        book = next((book for book in self.books if book['id'] == book_id), None)
        if book:
            print(f"Processing order for {customer_name} for book '{book['title']}'")
            self.send_notification(customer_name, f"Your order for '{book['title']}' has been processed.")
        else:
            print(f"Book with ID {book_id} not found")

    def send_notification(self, customer_name, message, contact, notification_type):
        if notification_type == "sms":
            print(f"Sending notification to {customer_name}: {message}")
        elif notification_type == "whatsapp":
            print(f"Sending notification to {customer_name}: {message}")
        else:
            raise Exception("Unknown notification type")



# after
class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price


class BookRepository:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books
    

class Notification:
    @staticmethod
    def send_via_whatsapp(customer_name, message, contact):
        print(f"Sending notification to {customer_name}: {message}")

    @staticmethod
    def send_sms(customer_name, message, contact):
        print(f"Sending notification to {customer_name}: {message}")

    # send_email
    # send_push_notification


class OrderProcessor:
    def __init__(self, book_repository, notifier):
        self.book_repository = book_repository
        self.notifier = notifier

    def process_order(self, book_id, customer_name):
        books = self.book_repository.get_books()
        book = next((book for book in books if book.book_id == book_id), None)
        if book:
            print(f"Processing order for {customer_name} for book '{book.title}'")
            self.notifier.send_notification(customer_name, f"Your order for '{book.title}' has been processed.")
        else:
            print(f"Book with ID {book_id} not found")

    # PhysicalBookOrderProcessor
    # EBookOrderProcessor
    # PreOrderProcessor
    # SubscriptionOrderProcessor
