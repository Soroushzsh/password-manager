from utils.password_manager import PasswordManager


def test_generate_password_length():
    password_manager = PasswordManager()
    password = password_manager.generate_password(length=10)
    assert len(password) == 10


def test_generate_password_symbols():
    password_manager = PasswordManager()
    password = password_manager.generate_password(length=8)
    assert any(symbol in password for symbol in PasswordManager.SYMBOLS)


def test_generate_password_uppercase():
    password_manager = PasswordManager()
    password = password_manager.generate_password(length=8)
    assert any(char.isupper() for char in password)


def test_generate_password_lowercase():
    password_manager = PasswordManager()
    password = password_manager.generate_password(length=8)
    assert any(char.islower() for char in password)


def test_generate_password_digits():
    password_manager = PasswordManager()
    password = password_manager.generate_password(length=8)
    assert any(char.isdigit() for char in password)


def test_generate_password_shuffle():
    password_manager = PasswordManager()
    password1 = password_manager.generate_password(length=8)
    password2 = password_manager.generate_password(length=8)
    assert password1 != password2


def test_generate_password_default_length():
    password_manager = PasswordManager()
    password = password_manager.generate_password()
    assert len(password) == 8
