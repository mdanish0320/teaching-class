# in this example, we will be showing
# 1. inheritance
# 2. property overriding
# 3. method overriding (polymorphism)

class Employee:

    raise_amount = 0.1  # 10 percent

    def __init__(self, first, last, salary):
        self.fname = first
        self.lname = last
        self.salary = salary

    def apply_raise(self):
        self.salary = self.salary + int(self.salary * self.raise_amount)


class Developer(Employee):
    # property overriding
    raise_amount = 0.3  # 30 percent

    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.prog_lang = prog_lang


class Manager(Employee):
    # property overriding
    raise_amount = 0.2  # 20 percent

    def __init__(self, first, last, salary, fuel_allowance):
        super().__init__(first, last, salary)
        self.fuel_allowance = fuel_allowance

    # method overriding
    def apply_raise(self):
        self.salary = self.salary + int(self.salary * self.raise_amount) + self.fuel_allowance
     
     
emp_1 = Employee("Shoaib", "Ali", 1000)
emp_1.apply_raise()
print(
    "Normal Employee:", emp_1.fname, emp_1.salary, "is a new salary w.r.t increase in 10%, old salary was 1000"
)


dev_1 = Developer('Muhammad', 'Danish', 1000, 'Python')
dev_1.apply_raise()
print(
    "Developer:", dev_1.fname, dev_1.salary, "is a new salary w.r.t increase in 30%, old salary was 1000"
)


mgr_1 = Manager('Fahad', 'Ali', 1000, 500)
mgr_1.apply_raise()
print(
    "Manager:", mgr_1.fname, mgr_1.salary, "is a new salary w.r.t increase in 20% and fule allowance, old salary was 1000"
)
