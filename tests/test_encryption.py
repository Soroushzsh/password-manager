import pytest
from cryptography.fernet import InvalidToken, Fernet

from utils.custom_encryption import FernetEncryptor


# Test the FernetEncryptor class
class TestFernetEncryptor:

    # Test encryption and decryption with valid key
    def test_valid_encryption_decryption(self):
        key = Fernet.generate_key()
        encryptor = FernetEncryptor(key)
        plaintext = "This is a secret message"
        
        # Encrypt the plaintext
        ciphertext = encryptor.encrypt(plaintext)

        # Decrypt the ciphertext and check if it matches the original plaintext
        decrypted_data = encryptor.decrypt(ciphertext)
        assert decrypted_data == plaintext

    # Test decryption with invalid key (should return None)
    def test_invalid_decryption(self):
        # Generate two different keys
        key1 = Fernet.generate_key()
        key2 = Fernet.generate_key()
        
        # Encrypt with one key and attempt decryption with another
        encryptor1 = FernetEncryptor(key1)
        encryptor2 = FernetEncryptor(key2)
        plaintext = "This is a secret message"
        
        ciphertext = encryptor1.encrypt(plaintext)
        
        # Attempt decryption with the wrong key
        decrypted_data = encryptor2.decrypt(ciphertext)
        assert decrypted_data is None
