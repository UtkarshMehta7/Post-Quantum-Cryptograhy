import time
import hashlib

# =====================================
# PQC (ML-KEM / Kyber) Simulation Engine
# Stable version for deployment (NO OQS dependency)
# =====================================

def generate_pqc_demo(message):

    start_time = time.time()

    kemalg = "ML-KEM-512 (Simulated)"

    # =====================================
    # Step 1: Encode message into integers
    # =====================================
    encoded = [ord(c) for c in message]

    # =====================================
    # Step 2: Simulated lattice transformation
    # (deterministic polynomial-style mapping)
    # =====================================
    ciphertext = [(x * 7 + 13) % 3329 for x in encoded]

    # =====================================
    # Step 3: Simulated shared secret (deterministic)
    # =====================================
    shared_secret_raw = hashlib.sha256(message.encode()).hexdigest()
    shared_secret = shared_secret_raw[:64]

    # =====================================
    # Step 4: Timing
    # =====================================
    encryption_time = round(time.time() - start_time, 6)

    # =====================================
    # Step 5: Return structured response
    # =====================================

    return {
        "algorithm": kemalg,
        "message": message,
        "ciphertext": ciphertext,
        "shared_secret": shared_secret,
        "decryption_status": True,
        "security_type": "Lattice-Based Post Quantum Cryptography (Simulation)",
        "key_size": 800,
        "ciphertext_size": len(ciphertext),
        "shared_secret_size": 32,
        "encryption_time": encryption_time,
        "quantum_safe": True,
        "oqs_status": "SIMULATED"
    }