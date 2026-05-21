import base64
import time

try:
    import oqs
    OQS_AVAILABLE = True
except Exception:
    OQS_AVAILABLE = False


# =====================================
# Real ML-KEM / Kyber PQC Demonstration
# =====================================

def generate_pqc_demo(message):

    # =====================================
    # Start Encryption Timer
    # =====================================

    start_time = time.time()

    # =====================================
    # ML-KEM-512 (CRYSTALS-Kyber)
    # =====================================

    kemalg = "ML-KEM-512"

    # =====================================
    # Check OQS Availability
    # =====================================

    if not OQS_AVAILABLE:

        return {
            "algorithm": kemalg,
            "message": message,
            "ciphertext": "OQS library not installed",
            "shared_secret": "Unavailable",
            "decryption_status": False,
            "security_type": "OQS Dependency Missing",
            "key_size": 800,
            "ciphertext_size": 768,
            "shared_secret_size": 32,
            "encryption_time": 0,
            "quantum_safe": True,
            "oqs_status": "NOT INSTALLED"
        }

    # =====================================
    # Real OQS Execution
    # =====================================

    try:

        with oqs.KeyEncapsulation(kemalg) as server:

            public_key = server.generate_keypair()

            with oqs.KeyEncapsulation(kemalg) as client:

                ciphertext, shared_secret_client = client.encap_secret(public_key)

            shared_secret_server = server.decap_secret(ciphertext)

    except Exception as error:

        return {
            "algorithm": kemalg,
            "message": message,
            "ciphertext": str(error),
            "shared_secret": "Execution Failed",
            "decryption_status": False,
            "security_type": "OQS Runtime Error",
            "key_size": 800,
            "ciphertext_size": 768,
            "shared_secret_size": 32,
            "encryption_time": 0,
            "quantum_safe": True,
            "oqs_status": "FAILED"
        }

    # =====================================
    # Encryption Timing
    # =====================================

    encryption_time = round(time.time() - start_time, 6)

    # =====================================
    # Base64 Encoding
    # =====================================

    ciphertext_base64 = base64.b64encode(ciphertext).decode()

    shared_secret_base64 = base64.b64encode(shared_secret_client).decode()

    # =====================================
    # Return Result
    # =====================================

    return {
        "algorithm": kemalg,
        "message": message,
        "ciphertext": ciphertext_base64,
        "shared_secret": shared_secret_base64,
        "decryption_status": shared_secret_client == shared_secret_server,
        "security_type": "Quantum Resistant",
        "key_size": len(public_key),
        "ciphertext_size": len(ciphertext),
        "shared_secret_size": len(shared_secret_client),
        "encryption_time": encryption_time,
        "quantum_safe": True,
        "oqs_status": "ACTIVE"
    }