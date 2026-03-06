# run only once
# we get a key
# use that key to encrypt or decrypt

from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key.decode())
