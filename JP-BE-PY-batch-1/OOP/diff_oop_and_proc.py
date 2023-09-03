# Procedural Programming

# Define initial variables
account_balance = {}

# Function to open an account


def open_account(account_number):
    account_balance[account_number] = 0
    print(f"Account {account_number} opened.")

# Function to deposit funds


def deposit(account_number, amount):
    if account_number in account_balance:
        account_balance[account_number] += amount
        print(f"Deposited {amount} to Account {account_number}.")
    else:
        print("Account not found.")

# Function to withdraw funds


def withdraw(account_number, amount):
    if account_number in account_balance:
        if account_balance[account_number] >= amount:
            account_balance[account_number] -= amount
            print(f"Withdrew {amount} from Account {account_number}.")
        else:
            print("Insufficient funds.")
    else:
        print("Account not found.")

# Function to check account balance


def check_balance(account_number):
    if account_number in account_balance:
        print(
            f"Account {account_number} balance: {account_balance[account_number]}")
    else:
        print("Account not found.")


# Usage
open_account(1001)
deposit(1001, 500)
withdraw(1001, 200)
check_balance(1001)


# Object-Oriented Programming

class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to Account {self.account_number}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from Account {self.account_number}.")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")


# Usage
account1 = BankAccount(1001)
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()


# Procedural Programming

# Define character attributes
character1 = {"name": "Alice", "health": 100, "attack": 20}
character2 = {"name": "Bob", "health": 90, "attack": 25}

# Function to attack a character


def attack(attacker, target):
    damage = attacker["attack"]
    target["health"] -= damage
    print(f"{attacker['name']} attacks {target['name']} for {damage} damage.")


# Usage
attack(character1, character2)
print(f"{character2['name']}'s health: {character2['health']}")


# Object-Oriented Programming

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_target(self, target):
        damage = self.attack
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage} damage.")

    def take_damage(self, damage):
        self.health -= damage

    def get_health(self):
        return self.health


# Usage
character1 = Character("Alice", 100, 20)
character2 = Character("Bob", 90, 25)

character1.attack_target(character2)
print(f"{character2.name}'s health: {character2.get_health()}")


# Procedural Programming

# Define products and shopping cart
products = []
shopping_cart = []

# Function to add a product to the shopping cart


def add_product_to_cart(product):
    shopping_cart.append(product)
    print(f"{product['name']} added to the shopping cart.")

# Function to calculate the total price in the shopping cart


def calculate_total_price():
    total_price = 0
    for product in shopping_cart:
        total_price += product['price']
    return total_price


# Usage
product1 = {"name": "Laptop", "price": 800}
product2 = {"name": "Headphones", "price": 50}

add_product_to_cart(product1)
add_product_to_cart(product2)

total_price = calculate_total_price()
print(f"Total price in the shopping cart: ${total_price}")


# Object-Oriented Programming

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)
        print(f"{product.name} added to the shopping cart.")

    def calculate_total_price(self):
        total_price = sum(product.price for product in self.cart)
        return total_price


# Usage
product1 = Product("Laptop", 800)
product2 = Product("Headphones", 50)

cart = ShoppingCart()
cart.add_product(product1)
cart.add_product(product2)

total_price = cart.calculate_total_price()
print(f"Total price in the shopping cart: ${total_price}")


# Procedural Programming

# Define products and shopping carts for two users
user1_cart = []
user2_cart = []

# Function to add a product to a user's shopping cart


def add_product_to_cart(user_cart, product):
    user_cart.append(product)
    print(f"{product['name']} added to the shopping cart.")

# Function to calculate the total price in a user's shopping cart


def calculate_total_price(user_cart):
    total_price = 0
    for product in user_cart:
        total_price += product['price']
    return total_price


# Usage
product1 = {"name": "Laptop", "price": 800}
product2 = {"name": "Headphones", "price": 50}

add_product_to_cart(user1_cart, product1)
add_product_to_cart(user2_cart, product2)

# User 1's total price
total_price_user1 = calculate_total_price(user1_cart)
print(f"User 1's total price in the shopping cart: ${total_price_user1}")

# User 2's total price
total_price_user2 = calculate_total_price(user2_cart)
print(f"User 2's total price in the shopping cart: ${total_price_user2}")


# Object-Oriented Programming

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)
        print(f"{product.name} added to the shopping cart.")

    def calculate_total_price(self):
        total_price = sum(product.price for product in self.cart)
        return total_price


# Usage
product1 = Product("Laptop", 800)
product2 = Product("Headphones", 50)

cart_user1 = ShoppingCart()
cart_user2 = ShoppingCart()

cart_user1.add_product(product1)
cart_user2.add_product(product2)

# User 1's total price
total_price_user1 = cart_user1.calculate_total_price()
print(f"User 1's total price in the shopping cart: ${total_price_user1}")

# User 2's total price
total_price_user2 = cart_user2.calculate_total_price()
print(f"User 2's total price in the shopping cart: ${total_price_user2}")


# Define employee data as separate variables
employees = []

# Function to add an employee


def add_employee(employee):
    employees.append(employees)
    # employee_names.append(name)
    # employee_salaries.append(salary)

# Function to calculate the total salary


def calculate_total_salary(employees):
    total_salaries = 0
    for employe_info in employees:
        total_salaries += employe_info['salary']
    return total_salaries


# Usage
add_employee({"name":"Alice", "salary":50000})
# add_employee({"name": "Bob", "salary": 60000})

total_salary = calculate_total_salary(employees)
print(f"Total salary of all employees: ${total_salary}")
