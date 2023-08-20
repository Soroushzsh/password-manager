import hashlib
import base64

from prettytable import PrettyTable
import pyperclip

from custom_validators import is_int, yes_or_no_validator
from password_manager import PasswordManager
from custom_encryption import FernetEncryptor


def display(header, data):
    table = PrettyTable()
    table.field_names = header
    for item in data:
        table.add_row([element for element in item])

    print(table)


def get_encryption_key():
    key = input('Enter encryption key: ')
    hash_object = hashlib.sha256(key.encode())
    hash_value = hash_object.digest()
    key = base64.b64encode(hash_value)
    return key


def copy_password(password):
    ans = input('Copy password to the clipboard?(y/n) ')
    while not yes_or_no_validator(ans):
        ans = input("Please enter 'y' for 'yes' and 'n' for 'no': ")
    if ans == 'y':
        pyperclip.copy(password)


def generate_new_password(db, key):
    password_length = input('Password length: ')
    while not is_int(password_length):
      password_length = input('Please enter a valid number for password length: ')
    else:
        new_password = PasswordManager.generate_password(length=int(password_length))
        print('Your new password is: ', new_password)
        copy_password(new_password)

        # fixme: separate this logic from this function
        ans = input('Do you want to save this password for new account?(y/n) ')
        while not yes_or_no_validator(ans):
            ans = input("Please enter 'y' for 'yes' and 'n' for 'no': ")
        if ans == 'y':
            add_new_account(db, key, password=new_password)


def check_for_duplicate_service_name(db, service_name):
    count = db.count(service_name=service_name)
    if count > 0:
        return True
    return False


def check_for_duplicate_username(db, service_name, username):
    count = db.count(service_name=service_name, username=username)
    if count > 0:
        return True
    return False


def get_account_address(db):
    while True:
        account_address = input('Account address: ')

        if not check_for_duplicate_service_name(db, account_address):
            return account_address
        
        ans = input("Another account with exact same address exists. \
            \nDo you want to continue with this address?(y/n) ")
        while not yes_or_no_validator(ans):
            ans = input("Please enter 'y' for 'yes' and 'n' for 'no': ")

        if ans == 'y':
            return account_address


def get_username(db, service_name):
    while True:
        username = input('Username: ')

        if not check_for_duplicate_username(db, service_name, username):
            return username

        ans = input("Another account in this service with exact same username exists. \
            \nDo you want to continue with this address?(y/n) ")
        while not yes_or_no_validator(ans):
            ans = input("Please enter 'y' for 'yes' and 'n' for 'no': ")

        if ans == 'y':
            return username


def add_new_account(db, key, password=None):
    account_address = get_account_address(db)
    username = get_username(db, account_address)

    if not password:
        password = input('Password: ')

    enc = FernetEncryptor(key=key)
    password = enc.encrypt(password)
    db.insert(account_address, username, password)

    print('New account saved successfully')


def update_password(db, key, account_id):
    print("""
    1- Generate new password
    2- Enter new password
    """)
    while True:
        try:
            op = int(input('Option number: '))
        except ValueError:
            print('Invalid input')
        else:
            break
    
    if op == 1:
        pass
    elif op == 2:
        pass
    else:
        print('Invalid option has been selected!')


def delete_account(db, account_id):
    ans = input('Are you sure you want to delete this account?(y/n) ')
    while not yes_or_no_validator(ans):
        ans = input("Please enter 'y' for 'yes' and 'n' for 'no': ")

    if ans == 'y':
        db.delete(account_id)
        print('Account deleted!')


def manage_account(db, key, account_id, password):
    print("""Choose an option to use:
    1- Copy password
    2- Update password
    3- Update username
    4- Delete
    """)

    while True:
        try:
            op = int(input('Option number: '))
        except ValueError:
            print('Invalid input')
        else:
            break
    
    if op == 1:
        copy_password(password)
    elif op == 2:
        update_password(db, key, account_id)
    elif op == 3:
        delete_account(account_id)
    else:
        print('Invalid option has been selected!')


def retrieve_account_info_by_id(db, key):
    service_id = input('Service ID: ')
    while not is_int(service_id):
        service_id = input('Please enter a valid number for service ID: ')
    result = db.retrieve_service_by_id(service_id)
    if not result:
        print('Account with this ID does not exist')
        return None
    
    password = result[2]
    enc = FernetEncryptor(key=key)
    password = enc.decrypt(password)
    if password is None:
        print("Can't retrieve account information with this encryption key")
    else:
        print('Your account info: \n')
        display(['Address', 'Username', 'Password'], [[result[0], result[1], password]])
        manage_account(db, key, service_id, password)


def retrieve_account_info_by_name(db, key):
    service_name = input('Service name: ')
    result = db.retrieve_by_service_name(service_name)
    if not result:
        print('Account with this ID does not exist')
        return None

    display(['ID', 'Address', 'Username'], result)
    

def show_all_accounts(db):
    services =  db.retrieve_all_services()
    if not services:
        print('No services have been added yet')
        return None

    display(["ID", 'Address', 'Username'], services)
