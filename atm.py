class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
    
    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Invalid withdrawal amount."


class ATM:
    def __init__(self, account):
        self.account = account
    
    def authenticate(self, pin):
        if self.account.pin == pin:
            return True
        else:
            return False
    
    def perform_transaction(self, pin, transaction_type, amount=0):
        if not self.authenticate(pin):
            return "Authentication failed. Invalid PIN."
        
        if transaction_type == 'balance':
            return f"Your balance is ${self.account.check_balance()}."
        elif transaction_type == 'deposit':
            return self.account.deposit(amount)
        elif transaction_type == 'withdraw':
            return self.account.withdraw(amount)
        else:
            return "Invalid transaction type."



account_number = input("Enter your account number: ")
pin = input("Enter your PIN: ")
initial_balance = float(input("Enter your initial balance: "))


account = Account(account_number, pin, initial_balance)
atm = ATM(account)

while True:
    print("\n1. Check Balance")
    print("\n2. Deposit Money")
    print("\n3. Withdraw Money")
    print("\n4. Exit")
    
    choice = input("\nEnter your choice: ")

    if choice == '1':
        print(atm.perform_transaction(pin=input("Enter PIN: "), transaction_type="balance"))
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        print(atm.perform_transaction(pin=input("Enter PIN: "), transaction_type="deposit", amount=amount))
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        print(atm.perform_transaction(pin=input("Enter PIN: "), transaction_type="withdraw", amount=amount))
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
