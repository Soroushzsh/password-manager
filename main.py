from utils.functions import (generate_new_password, add_new_account, retrieve_account_info_by_id, retrieve_account_info_by_name,
                       show_all_accounts, get_encryption_key)
from utils.custom_validators import yes_or_no_validator
from utils.database import Database


def main(db, key):
    print("""Choose an option to use:
    1- Generate a new password
    2- Add new account info
    3- Retrieve existing account info by ID
    4- Retrieve existing account info by name
    5- Show all existing accounts
    6- Change encryption key
    """)
    while True:
        try:
            op = int(input('Option number: '))
        except ValueError:
            print('Invalid input')
        else:
            break
    
    # todo: how can I implement this using open-closed principle?
    if op == 1:
        generate_new_password(db, key)
    elif op == 2:
        add_new_account(db, key)
    elif op == 3:
        retrieve_account_info_by_id(db, key)
    elif op == 4:
        retrieve_account_info_by_name(db, key)
    elif op == 5:
        show_all_accounts(db)
    elif op == 6:
        key = get_encryption_key()
    else:
        print('Invalid option has been selected!')

    cont = input('Do you want to continue?(y/n)')
    while not yes_or_no_validator(cont):
        cont = input("Please enter 'y' for 'yes' and 'n': ")
    if cont == 'y':
        main(db, key)
    else:
        print('Bye')


if __name__ == '__main__':
    db = Database('db.sqlite')
    key = get_encryption_key()
    main(db, key)
