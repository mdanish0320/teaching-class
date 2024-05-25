# bank transaction
balance = 0
affiliated_card = True # meezan
is_senior_citizen = True
is_govt_employee = True
high_grade = True
my_profit = 10


print("initital balance", balance)

withdraw_amount = 50

if balance < withdraw_amount:
    print("insufficient balance")
    
deposit_amount = 500

# balance = balance + deposit_amount
balance += deposit_amount

print("after first depost:", balance)

withdraw_amount = 50
if withdraw_amount <= balance and (affiliated_card == True or is_senior_citizen):
    balance = balance - withdraw_amount
    print("after withdraw:", balance)
elif is_govt_employee and withdraw_amount <= balance:
    if high_grade:
        balance = balance - withdraw_amount
        print("after withdraw:", balance)
    elif is_govt_employee and withdraw_amount <= balance + my_profit:
       balance -= deposit_amount + my_profit