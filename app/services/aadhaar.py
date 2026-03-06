from cryptography.fernet import Fernet
from dotenv import load_dotenv
from app.core.config import AADHAAR_SECRET_KEY
load_dotenv()

key = AADHAAR_SECRET_KEY

if key is None:
    raise ValueError("AADHAAR_SECRET_KEY not set")

cipher = Fernet(key.encode())

def encrypt_aadhar(aadhar_number: str) -> str:
    encrypted = cipher.encrypt(aadhar_number.encode())
    return encrypted.decode()

# currently not in use, will use only when required
def decrypt_aadhar(encrypted_aadhar: str) -> str:
    decrypted = cipher.decrypt(encrypted_aadhar.encode())
    return decrypted.decode()