import datetime

print("Welcome to Vishal International Bank!")

# Function to create account
def create_account():
    name = input("Enter your name: ")
    initial_deposit = float(input("Enter your initial deposit: "))
    password = input("Enter a password: ")
    account_number = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))  # Unique account number
    with open("accounts.txt", "a") as f:
        f.write(f"{account_number},{name},{password},{initial_deposit}\n")
    print(f"Account created successfully! Your account number is {account_number}")

# Function to login
def login():
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")
    with open("accounts.txt", "r") as f:
        accounts = f.readlines()
    for account in accounts:
        acc_num, name, acc_pass, balance = account.strip().split(",")
        if acc_num == account_number and acc_pass == password:
            print(f"Login successful! Welcome {name}")
            user_menu(acc_num, float(balance))
            return
    print("Invalid credentials!")

# Function for user operations
def user_menu(account_number, balance):
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            log_transaction(account_number, "Deposit", amount)
            update_balance(account_number, balance)
            print(f"Deposit successful! Current balance: {balance}")
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance!")
            else:
                balance -= amount
                log_transaction(account_number, "Withdrawal", amount)
                update_balance(account_number, balance)
                print(f"Withdrawal successful! Current balance: {balance}")
        elif choice == "3":
            print(f"Current balance: {balance}")
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

# Function to log transactions
def log_transaction(account_number, trans_type, amount):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    with open("transactions.txt", "a") as f:
        f.write(f"{account_number},{trans_type},{amount},{date}\n")

# Function to update balance in accounts.txt
def update_balance(account_number, new_balance):
    with open("accounts.txt", "r") as f:
        accounts = f.readlines()
    with open("accounts.txt", "w") as f:
        for account in accounts:
            acc_num, name, acc_pass, balance = account.strip().split(",")
            if acc_num == account_number:
                f.write(f"{acc_num},{name},{acc_pass},{new_balance}\n")
            else:
                f.write(account)

# Main Menu
def main():
    while True:
        print("\n1. Create Account\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()