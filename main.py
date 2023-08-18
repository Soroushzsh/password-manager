from functions import generate_new_password, add_new_account, retrieve_account_info, show_all_accounts
from custom_validators import yes_or_no_validator
from database import Database


# todo: copy password to the clipboard
# todo: write test with pytest

def main(db):
    print("""Choose an option to use:
    1- Generate a new password
    2- Add new account info
    3- Retrieve existing account info
    4- Show all existing accounts
    """)
    while True:
        try:
            op = int(input('Option number: '))
        except ValueError:
            print('Invalid input')
        else:
            break

    if op == 1:
        new_password = generate_new_password()
        print('Your password: ', new_password)
        ans = input('Do you want to save it?(y/n)')
        while not yes_or_no_validator(ans):
            ans = input("Please enter 'y' for 'yes' and 'n' for 'no'")
        if ans == 'y':
            add_new_account(db, password=new_password)
    elif op == 2:
        add_new_account(db)
    elif op == 3:
        account_info = retrieve_account_info(db)
        if account_info:
            print('Your account info: ', account_info)
        else:
            print('Account with this ID does not exist')
    elif op == 4:
        print('Your accounts: \n', show_all_accounts(db))
    else:
        print('Invalid option has been selected!')

    cont = input('Do you want to continue?(y/n)')
    while not yes_or_no_validator(cont):
        cont = input("Please enter 'y' for 'yes' and 'n'")
    if cont == 'y':
        main(db)
    else:
        print('Bye')


if __name__ == '__main__':
    db = Database('db.sqlite')
    main(db)
