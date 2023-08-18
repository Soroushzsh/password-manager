from cryptography.fernet import Fernet


class FernetEncryptor:
    def __init__(self, key=None):
        if key is None:
            key = Fernet.generate_key()
        self.key = key
        self.cipher_suite = Fernet(self.key)

    def encrypt(self, plaintext):
        ciphertext = self.cipher_suite.encrypt(plaintext.encode())
        return ciphertext

    def decrypt(self, ciphertext):
        decrypted_data = self.cipher_suite.decrypt(ciphertext)
        return decrypted_data.decode()
