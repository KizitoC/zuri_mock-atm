def user_account_number_validation(user_account_number):
    """Validate user account number"""
    if user_account_number:  # Check if account number was entered
        if len(str(user_account_number)) == 10:  # Check if account number is 10 digits
            try:
                int(user_account_number)
                return True
            except ValueError:  # Except an error if user entered invalid account number
                print("\nInvalid account number! Please make "
                      "sure account number is a number.")
                return False
            except TypeError:
                print("\nInvalid account number type! Please make "
                      "sure account number is a number.")
        else:
            print("\nAccount number must be up to 10 digits.")
            return False
    else:  # Check if nothing was entered
        print("Account number is a required field.\n")
        return False


def bank_operation_validation(selected_option):
    """Validate bank operation input from user"""
    if selected_option:  # Check if an option was selected
        try:
            int(selected_option)
            return True
        except ValueError:
            print("Input must be a number.\n")
            return False
        except TypeError:
            print("Input must be an integer.\n")
    else:
        print("Input is required to proceed.\n")
        return False
