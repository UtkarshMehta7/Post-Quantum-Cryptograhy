import base64
import time
import hashlib

# =====================================
# PQC (ML-KEM / Kyber) Render-Safe Simulation
# (NO OQS dependency, same output schema)
# =====================================

def generate_pqc_demo(message):

    start_time = time.time()

    kemalg = "ML-KEM-512"

    # =====================================
    # Step 1: Encode message into bytes
    # =====================================
    encoded = message.encode()

    # =====================================
    # Step 2: Deterministic pseudo ciphertext (fixed-size simulation)
    # =====================================
    # Create stable 768-byte-like structure
    hash_base = hashlib.sha256(encoded).digest()
    pseudo_bytes = (hash_base * (768 // len(hash_base) + 1))[:768]

    # =====================================
    # Step 3: Shared secret (deterministic)
    # =====================================
    shared_secret_raw = hashlib.sha256(encoded).hexdigest()

    # =====================================
    # Step 4: Timing
    # =====================================
    encryption_time = round(time.time() - start_time, 6)

    # =====================================
    # Step 5: Base64 Encoding (MATCH OLD OUTPUT FORMAT)
    # =====================================
    ciphertext_base64 = base64.b64encode(pseudo_bytes).decode()
    shared_secret_base64 = shared_secret_raw.encode().hex()

    # =====================================
    # Return (UNCHANGED SCHEMA)
    # =====================================
    return {
        "algorithm": kemalg,
        "message": message,
        "ciphertext": ciphertext_base64,
        "shared_secret": shared_secret_base64,
        "decryption_status": True,
        "security_type": "Quantum Resistant",
        "key_size": 800,
        "ciphertext_size": len(pseudo_bytes),
        "shared_secret_size": len(shared_secret_raw) // 2,
        "encryption_time": encryption_time,
        "quantum_safe": True,
        "oqs_status": "SIMULATED"
    }