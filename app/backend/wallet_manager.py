from cryptography.fernet import Fernet

class WalletManager:
    def __init__(self, encryption_key):
        self.cipher = Fernet(encryption_key)

    def encrypt_private_key(self, private_key):
        return self.cipher.encrypt(private_key.encode())

    def decrypt_private_key(self, encrypted_key):
        return self.cipher.decrypt(encrypted_key).decode()