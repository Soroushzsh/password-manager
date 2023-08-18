import pytest
from fernet_encryptor import FernetEncryptor


class TestFernetEncryptor:
    @pytest.fixture
    def encryptor(self):
        key = b'V2KNo9nZmJXrYOXE-HFz7PVkxJcd4iwfKHqsPRrwKZw='
        return FernetEncryptor(key)

    def test_encrypt_and_decrypt(self, encryptor):
        plaintext = "This is a secret message."
        encrypted_data = encryptor.encrypt(plaintext)
        decrypted_data = encryptor.decrypt(encrypted_data)
        assert decrypted_data == plaintext

if __name__ == "__main__":
    pytest.main()
