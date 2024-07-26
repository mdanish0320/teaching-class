from abc import abc, abstractmethod

# before
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

class Notifier:
    @abstractmethod
    def send(customer_name, message, contact):
        pass

class SMSNotifier(Notifier):
    
    def send(customer_name, message, contact):
        print(f"Sending message to {customer_name}: {message} on {contact}")


class WhatsAppNotifier(Notifier):
    
    def send(customer_name, message, contact):
        print(f"Sending email to {customer_name}: {message} on {contact}")

class EmailNotifier(Notifier):
    
    def send(customer_name, message, email):
        print(f"Sending message to {customer_name}: {message} on {email}")







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

class Notifier:
    @abstractmethod
    def send(customer_name, message):
        pass


class SMSNotifier(Notifier):
    def __init__(self, contact):
        self.contact = contact
    
    def send(self, customer_name, message):
        print(f"Sending message to {customer_name}: {message} on {self.contact}")


class WhatsAppNotifier(Notifier):
    def __init__(self, contact):
        self.contact = contact

    def send(self, customer_name, message):
        print(f"Sending message to {customer_name}: {message} on {self.contact}")


class EmailNotifier(Notifier):
    def __init__(self, email):
        self.email = email
    
    def send(self, customer_name, message):
        print(f"Sending message to {customer_name}: {message} on {self.email}")