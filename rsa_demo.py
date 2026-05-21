

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import time

try:
    from Crypto import Random
    RSA_AVAILABLE = True
except Exception:
    RSA_AVAILABLE = False


def generate_rsa_demo(message):

    # =====================================
    # Check RSA Availability
    # =====================================

    if not RSA_AVAILABLE:

        return {
            "algorithm": "RSA",
            "original_message": message,
            "encrypted_message": "RSA library unavailable",
            "decrypted_message": "Unavailable",
            "key_size": "2048-bit",
            "ciphertext_size": 256,
            "encryption_time": 0,
            "quantum_safe": False,
            "rsa_status": "NOT AVAILABLE"
        }

    # =====================================
    # Generate RSA Keys
    # =====================================

    try:

        key = RSA.generate(2048)

        private_key = key
        public_key = key.publickey()

    except Exception as error:

        return {
            "algorithm": "RSA",
            "original_message": message,
            "encrypted_message": str(error),
            "decrypted_message": "RSA Execution Failed",
            "key_size": "2048-bit",
            "ciphertext_size": 256,
            "encryption_time": 0,
            "quantum_safe": False,
            "rsa_status": "FAILED"
        }

    # =====================================
    # Create Cipher Object
    # =====================================

    cipher_encrypt = PKCS1_OAEP.new(public_key)
    cipher_decrypt = PKCS1_OAEP.new(private_key)

    # =====================================
    # Start Encryption Timer
    # =====================================

    start_time = time.time()

    # =====================================
    # Encrypt Message
    # =====================================

    encrypted_message = cipher_encrypt.encrypt(message.encode())
    encryption_time = round(time.time() - start_time, 6)

    # =====================================
    # Decrypt Message
    # =====================================

    decrypted_message = cipher_decrypt.decrypt(encrypted_message)

    # =====================================
    # Convert Encrypted Data to Base64
    # =====================================

    encrypted_base64 = base64.b64encode(encrypted_message).decode()

    # =====================================
    # Return Result
    # =====================================

    return {
        "algorithm": "RSA",
        "original_message": message,
        "encrypted_message": encrypted_base64,
        "decrypted_message": decrypted_message.decode(),
        "key_size": "2048-bit",
        "ciphertext_size": len(encrypted_message),
        "encryption_time": encryption_time,
        "quantum_safe": False,
        "rsa_status": "ACTIVE"
    }