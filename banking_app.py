import random
import datetime

accounts = {}


def generate_account_number():
    while True:
        account_number = str(random.randint(10000000, 99999999))
        if account_number not in accounts:
            return account_number


def create_account():
    print("\n====== CREATE NEW ACCOUNT ======")

    while True:
        acc_Holder_name = input("Enter account holder name:").strip()
        if acc_Holder_name:
            break
        print("Error: Account holder name cannot be empty.")

    while True:
        try:
            initial_balance = float(input("Enter initial deposit amount: Rs"))
            if initial_balance < 100:
                print("Error: Initial deposit cannot below 100 Rupees")
                continue
            break
        except ValueError:
            print("Error: Please enter above 100 Ruppes amount")

    account_number = generate_account_number()

    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    accounts[account_number] = {
        'acc_holder_name': acc_Holder_name,
        'balance': initial_balance,
        'transactions': [
            {
                'type': 'DEPOSIT',
                'amount': initial_balance,
                'timestamp': timestamp,
                'description': 'Initial deposit'
            }
        ] if initial_balance >= 100 else []
    }

    print("\n Account created successfully!")
    print(f"Account Number:{account_number}")
    print(f"Acc_Holder_Name:{acc_Holder_name}")
    print(f"Initial Balance: Rs{initial_balance:.2f}")

    return account_number

def deposit_money():
    print("\n====== DEPOSIT MONEY ======")

    account_number= input("Enter account number:").strip()

    if account_number not in accounts:
        print("Error: Account not found.")
        return
    
    while True:
        try:
            amount=float(input("Enter deposit amount: Rs."))