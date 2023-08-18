from custom_validators import is_int
from password_manager import PasswordManager


def generate_new_password():
    password_length = input('Password length: ')
    while not is_int(password_length):
      password_length = input('Please enter a valid number for password length: ')
    else:
        return PasswordManager.generate_password(length=int(password_length))


def add_new_account(db, password=None):
    # todo: check if any account with the same id already exists
    account_id = input('Account ID: ')
    username = input('Username: ')
    if not password:
        password = input('Password: ')

    db.insert(account_id, username, password)
    print('New account saved successfully')


def retrieve_account_info(db):
    account_id = input('Account ID: ')
    return db.retrieve_by_service_name(account_id)


def show_all_accounts(db):
    return db.retrieve_all_services()
