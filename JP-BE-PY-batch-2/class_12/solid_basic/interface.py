"""
I - Interface Segregation Principle (ISP):

Clients should not be forced to depend on interfaces they do not use. 

This principle encourages the creation of more specific interfaces 
rather than a single, large, general-purpose interface. 

It helps reduce the impact of changes and makes the code more modular and easier to understand.
"""
from abc import abc, abstractmethod

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
    
    @abstractmethod
    def validate_phone_number(self, phone_number):
        # Implementation for validating a phone number
        pass


class SMSNotifier(Notifier):
    def __init__(self, contact):
        self.contact = contact
    
    def send(self, customer_name, message):
        print(f"Sending message to {customer_name}: {message} on {self.contact}")

    def validate_phone_number(self, phone_number):
        return super().validate_phone_number(phone_number)


class WhatsAppNotifier(Notifier):
    def __init__(self, contact):
        self.contact = contact

    def send(self, customer_name, message):
        print(f"Sending message to {customer_name}: {message} on {self.contact}")

    def validate_phone_number(self, phone_number):
        raise Exception("The method is not implemented")


class EmailNotifier(Notifier):
    def __init__(self, email):
        self.email = email
    
    def send(self, customer_name, message):
        print(f"Sending message to {customer_name}: {message} on {self.email}")










# after
from abc import ABC, abstractmethod

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
    
    

class ISMSNotifier(Notifier):
    @abstractmethod
    def validate_phone_number(self, phone_number):
        # Implementation for validating a phone number
        pass


class SMSNotifier(ISMSNotifier):
    def __init__(self, contact):
        self.contact = contact
    
    def send(self, customer_name, message):
        print(f"Sending message to {customer_name}: {message} on {self.contact}")

    def validate_phone_number(self, phone_number):
        return super().validate_phone_number(phone_number)


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