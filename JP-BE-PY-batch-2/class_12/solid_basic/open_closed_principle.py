"""
O - Open/Closed Principle (OCP):

Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. 
This means you should be able to add new functionality without altering existing code, 
usually by using interfaces, abstract classes, or dependency injection.
"""
from abc import abc, abstractmethod

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
        print(f"Sending SMS to {customer_name}: {message}")


class WhatsAppNotifier(Notifier):
    
    def send(customer_name, message, contact):
        print(f"Sending email to {customer_name}: {message}")
        

class OrderProcessor:
    def __init__(self, book_repository, notifier):
        self.book_repository = book_repository
        self.notifier = notifier

    def process_physical_order(self, book_id, customer_name, address):
        book = next((book for book in self.book_repository.get_books() if book.book_id == book_id), None)
        if book:
            print(f"Processing physical book order for {customer_name} for book '{book.title}'")
            # Additional steps for physical book order
            self.notifier.send_notification(customer_name, f"Your physical book '{book.title}' has been shipped to {address}.")
        else:
            print(f"Book with ID {book_id} not found")

    def process_ebook_order(self, book_id, customer_name, email):
        book = next((book for book in self.book_repository.get_books() if book.book_id == book_id), None)
        if book:
            print(f"Processing e-book order for {customer_name} for book '{book.title}'")
            # Additional steps for e-book order
            download_link = f"http://example.com/download/{book_id}"
            self.notifier.send_notification(customer_name, f"Your e-book '{book.title}' is ready. Download it from {download_link}.")
        else:
            print(f"Book with ID {book_id} not found")


# Usage Example
book_repo = BookRepository()
email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()

order_processor = OrderProcessor(book_repo, email_notifier)

# Adding books to the repository
book_repo.add_book(Book(1, "Physical Book Title", "Author A", 20.0))
book_repo.add_book(Book(2, "E-Book Title", "Author B", 10.0))

# Processing orders
order_processor.process_physical_order(1, "John Doe", "123 Street Name")
order_processor.process_ebook_order(2, "Jane Doe", "jane.doe@example.com")
