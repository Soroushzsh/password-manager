import pytest
# from unittest.mock import patch
import getpass
from utils.functions import (display, get_encryption_key, copy_password, 
                        check_for_duplicate_service_name, check_for_duplicate_username,
                        get_account_address, get_username, add_new_account)

# todo: getpass function mocking not working
# Mock the getpass function for testing get_encryption_key
def test_get_encryption_key(monkeypatch):
    def mock_getpass():
        #assert prompt == "Enter encryption key: "
        return 'mysecretkey'

    # Monkeypatch the getpass.getpass function with the custom implementation
    monkeypatch.setattr(getpass, 'getpass', mock_getpass)
    key = get_encryption_key()

    assert key == b'47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU='


# # Mock the input function for testing get_account_address
# @patch('builtins.input', side_effect=['Service1', 'n', 'Service2', 'y'])
# def test_get_account_address():
#     # Simulate user input for service names
#     # First input: Service1 (no duplicate)
#     # Second input: Service2 (duplicate but user confirms)

#     # Mock the check_for_duplicate_service_name function
#     with patch('your_module.check_for_duplicate_service_name', return_value=False) as mock_check:
#         address = get_account_address(None)  # Pass None for db (not used in this test)
#         assert address == 'Service1'
#         mock_check.assert_called_once_with(None, 'Service1')

#     with patch('your_module.check_for_duplicate_service_name', side_effect=[True, False]) as mock_check:
#         address = get_account_address(None)  # Pass None for db (not used in this test)
#         assert address == 'Service2'
#         assert mock_check.call_count == 2
#         assert mock_check.call_args_list == [((None, 'Service2'),), ((None, 'Service2'),)]

# # Mock the input function for testing get_username
# @patch('builtins.input', side_effect=['User1', 'n', 'User2', 'y'])
# def test_get_username():
#     # Simulate user input for usernames
#     # First input: User1 (no duplicate)
#     # Second input: User2 (duplicate but user confirms)

#     # Mock the check_for_duplicate_username function
#     with patch('your_module.check_for_duplicate_username', return_value=False) as mock_check:
#         username = get_username(None, 'Service1')  # Pass None for db (not used in this test)
#         assert username == 'User1'
#         mock_check.assert_called_once_with(None, 'Service1', 'User1')

#     with patch('your_module.check_for_duplicate_username', side_effect=[True, False]) as mock_check:
#         username = get_username(None, 'Service1')  # Pass None for db (not used in this test)
#         assert username == 'User2'
#         assert mock_check.call_count == 2
#         assert mock_check.call_args_list == [((None, 'Service1', 'User2'),), ((None, 'Service1', 'User2'),)]

# # Mock the input and copy functions for testing copy_password
# @patch('builtins.input', side_effect=['y'])
# @patch('pyperclip.copy')
# def test_copy_password(mock_copy, mock_input):
#     copy_password('MySecretPassword')
#     mock_copy.assert_called_once_with('MySecretPassword')

# # Mock the check_for_duplicate_service_name function for testing add_new_account
# @patch('your_module.check_for_duplicate_service_name', return_value=False)
# def test_add_new_account(mock_check):
#     # Mock the input function for user input
#     with patch('builtins.input', side_effect=['Service1', 'User1', 'MySecretPassword']) as mock_input:
#         # Mock the FernetEncryptor class for testing the encryption
#         with patch('your_module.FernetEncryptor') as mock_encryptor:
#             add_new_account(None, None)  # Pass None for db and key (not used in this test)
#             mock_encryptor.assert_called_once_with(key=None)
#             mock_encryptor.return_value.encrypt.assert_called_once_with('MySecretPassword')
