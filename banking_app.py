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

    account_number = input("Enter account number:").strip()

    if account_number not in accounts:
        print("Error: Account not found.")
        return

    while True:
        try:
            amount = float(input("Enter deposit amount: Rs."))
            if amount <= 0:
                print("Error: Deposit amount must be positive.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid amount.")

    accounts[account_number]['balance'] += amount

    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    accounts[account_number]['transactions'].append({
        'type': 'DEPOSIT',
        'amount': amount,
        'timestamp': timestamp,
        'description': 'Deposit'
    })

    print("\n Deposit Successful")
    print(f"New Balance: Rs.{accounts[account_number]['balance']:.2f}")


def withdraw_money():
    print("\n====== WITHDRAW MONEY ======")

    account_number = input("Enter account number:").strip()

    if account_number not in accounts:
        print("Error: Account not found.")
        return

    while True:
        try:
            amount = float(input("Enter withdrawal amount:Rs."))
            if amount <= 0:
                print("Error: Withdrawal amount must be positive.")
                continue
            if amount > accounts[account_number]['balance']:
                print("Error:Insufficient funds.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number.")

    accounts[account_number['balance']] -= amount

    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    accounts[account_number]['transactions'].append({
        'type': 'WITHDRAWAL',
        'amount': amount,
        'timestamp': timestamp,
        'description': 'Withdrawal'
    })

    print("\nWithdrawal Successful")
    print(f"New Balance:Rs.{accounts[account_number]['balance']:.2f}")


def check_balance():
    print("\n====== CHECK BALANCE ======")

    account_number = input("Enter account number:").strip()

    if account_number not in accounts:
        print("Error: Account not found.")
        return

    account = accounts[account_number]
    print(f"\nAccount Holder:{account['acc_holder_name']}")
    print(f"Account Number:{account_number}")
    print(f"Current Balance:Rs.{account['balance']:.2f}")


def Transaction_History():
    print("\n====== TRANSACTION HISTORY ======")

    account_number = input("Enter account number:").strip()

    if account_number not in accounts:
        print("Error:Account not found.")
        return

    account = accounts[account_number]

    if not account['transactions']:
        print("\nNo transactions found for this account.")
        return

    print(
        f"\nTransaction History for Account{account_number}({account['acc_holder_name']}):")
    print("="*80)
    print(f"{'Type':<12}{'Amount':<12}{'Date & Time':<22}{'Description'}")
    print("-"*80)

    for transaction in account['transactions']:
        print(
            f"{transaction['type']:<12}Rs.{transaction['amount']:<11.2f}{transaction['timestamp']:<22}{transaction['description']}")

    print("="*80)


def Transfer_money():
    print("\n====== TRANSFER MONEY ======")

    source_account = input("Enter source account number:").strip()

    if source_account not in accounts:
        print("Error:Source account not found. ")
        return

    transfer_account = input("Enter transfer account number:").strip()

    if transfer_account not in accounts:
        print("Error: Transfer account not found.")
        return

    if source_account == transfer_account:
        print("Error:Source and transfer accounts cannot be the same.")
        return

    while True:
        try:
            amount = float(input("Enter transfer amount: Rs."))
            if amount <= 0:
                print("Error: Transfer amount must be positive.")
                continue
            if amount > accounts[source_account]['balance']:
                print("Error: Insufficient funds.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number.")

    accounts[source_account]['balance'] -= amount

    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    accounts[source_account]['transactions'].append({
        'type': 'TRANSFER OUT',
        'amount': amount,
        'timestamp': timestamp,
        'description': f'Transfer to Account{transfer_account}'

    })

    accounts[transfer_account]['balance'] += amount

    accounts[transfer_account]['transaction'].append({
        'type': 'TRANSFER IN',
        'amount': amount,
        'timestamp': timestamp,
        'description': f'Transfer from Account{source_account}'
    })

    print("\nTransfer Successful")
    print(
        f"Source Account ({source_account}) New Balance: Rs.{accounts[source_account]['balance']:.2f}")
    print(
        f"Transfer Account ({transfer_account}) New Balance: Rs.{accounts[transfer_account]['balance']:.2f}")


def display_menu():

    print("\n"+"="*40)
    print("BANK MANAGEMENT SYSTEM".center(40))
    print("="*40)
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Transfer Money")
    print("7. Exit")
    print("="*40)

def main():
    print("\n Welcome to the Mini Banking Application!")

    while True:
        display_menu()

        try:
            choice=int(input("Enetr your choice(1-7):"))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        if choice == 1:
            create_account()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            Transaction_History()
        elif choice == 6:
            Transfer_money()
        elif choice == 7:
            print("\n Thank you for using our banking system. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 7.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
