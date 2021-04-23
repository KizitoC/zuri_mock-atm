# A mock ATM program that receives user details, generates an account number
# for the user, validates it and allows them perform banking operations
# like Deposit, Withdrawal, as well as a complaint feature.
# Author: Kizito Ofoegbu

from datetime import datetime
from random import randrange
from sys import exit
from input_validation import user_account_number_validation, bank_operation_validation

# Display the current date and time.
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M")
print(current_time)

user_database = {}  # A dictionary for storing user details.


def zuri_bank():
    """A simple attempt to model a Banking System"""
    print("Welcome to Bank Zuri\n")
    have_account = int(input("Do you have an account with us?"
                             "\nEnter (1) for yes or (2) for no:\n"))

    # Check if user has an account with the bank.
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("You have selected an invalid option.\n")
        zuri_bank()


def register():
    """The bank registration function"""
    print("\n******** Register ********")

    user_email = input("Enter your email address:\n")
    first_name = input("Enter your first name:\n")
    last_name = input("Enter your last name:\n")
    password = input("Enter a password:\n")

    # Create an account number and set default account balance for the user.
    account_number = generate_account_number()
    account_bal = 0

    # Add user details to the dictionary database.
    user_database[account_number] = [
        first_name,
        last_name,
        user_email,
        password,
        account_bal,
    ]

    print("\nYour account has been created")
    print("== ==== ====== ===== === =====")
    print(f"Your account number is {account_number}. Please keep it safe.")
    print("== ==== ====== ===== === =====")
    login()


def login():
    """The bank login function"""
    print("\n******** Login ********")

    # Receive account number from user and validate it.
    user_account_number = input("Please enter your account number:\n")
    is_validated = user_account_number_validation(user_account_number)

    if is_validated:
        user_password = input("Enter your password:\n")

        for accountNumber, user_details in user_database.items():
            if accountNumber == int(user_account_number):
                if user_details[3] == user_password:
                    bank_operation(user_details)
                else:
                    print("Invalid account number or password!")
            else:
                print("Invalid account number or password!")
        login()
    else:
        zuri_bank()


def bank_operation(user):
    """The bank operation function"""
    print(f"\nWelcome, {user[0]} {user[1]}")

    # Receive input from user and validate it
    selected_option = input("What operation would you like to perform?"
                            "\nEnter (1) for Deposit (2) Withdrawal "
                            "(3) Complaint (4) Logout\n")
    is_validated = bank_operation_validation(selected_option)

    if is_validated:
        if int(selected_option) == 1:
            deposit(user)
        elif int(selected_option) == 2:
            withdrawal(user)
        elif int(selected_option) == 3:
            complaint(user)
        elif int(selected_option) == 4:
            logout()
        else:
            print("You selected an invalid option")
            bank_operation(user)
    else:
        zuri_bank()


def deposit(user_details):
    """The bank deposit function"""
    amount_deposit = eval(input("\nHow much would you "
                                "like to deposit?\n"))
    user_details[4] += amount_deposit
    print(f"Deposit Successful! Your account balance is "
          f"\u20a6{account_balance(user_details)}")

    choice = int(input("\nWould you like to perform another transaction?"
                       "\nEnter (1) for Yes or (2) for No\n"))

    if choice == 1:
        bank_operation(user_details)
    elif choice == 2:
        print("\nThank you for banking with us.")
        exit()
    else:
        print("\nYou selected an invalid option!")
        bank_operation(user_details)


def withdrawal(user_details):
    """The bank withdrawal function"""
    withdraw_cash = eval(input("\nHow much would you "
                               "like to withdraw?\n"))
    if withdraw_cash <= user_details[4]:
        user_details[4] -= withdraw_cash
        print(f"Withdrawal successful! Your account balance is "
              f"\u20a6{account_balance(user_details)}")
    else:
        print("Withdrawal unsuccessful! You have insufficient funds!")
        print(f"Your account balance is \u20a6{account_balance(user_details)}")

    choice = int(input("\nWould you like to perform another transaction?"
                       "\nEnter (1) for Yes or (2) for No\n"))

    if choice == 1:
        bank_operation(user_details)
    elif choice == 2:
        print("\nThank you for banking with us.")
        exit()
    else:
        print("\nYou selected an invalid option!")
        bank_operation(user_details)


def complaint(user_details):
    """The complaint function"""
    user_complaint = input("\nWhat issue would you like to report?\n")
    if user_complaint:
        print("Your complaint has been recorded.")

    choice = int(input("\nWould you like to perform another transaction?"
                       "\nEnter (1) for Yes or (2) for No\n"))

    if choice == 1:
        bank_operation(user_details)
    elif choice == 2:
        print("\nThank you for banking with us.")
        exit()
    else:
        print("\nYou selected an invalid option!")
        bank_operation(user_details)


def logout():
    """The logout function"""
    print("\nThank you for banking with us.")
    exit()


def account_balance(user_details):
    """The account balance function"""
    return user_details[4]


def generate_account_number():
    """The account number generator function"""
    return randrange(1111111111, 9999999999)


zuri_bank()
