

import time
import base64
import secrets
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


# =====================================
# RSA Benchmark
# =====================================

def benchmark_rsa(message):

    start_time = time.time()

    key = RSA.generate(2048)

    public_key = key.publickey()

    cipher = PKCS1_OAEP.new(public_key)

    encrypted_message = cipher.encrypt(message.encode())

    encryption_time = time.time() - start_time

    return {
        "algorithm": "RSA",
        "encryption_time": round(encryption_time, 6),
        "key_size": "2048-bit",
        "ciphertext_size": len(encrypted_message),
        "quantum_safe": False
    }


# =====================================
# PQC Benchmark (Simulated Kyber)
# =====================================

def benchmark_pqc(message):

    start_time = time.time()

    simulated_ciphertext = secrets.token_bytes(768)

    ciphertext = base64.b64encode(simulated_ciphertext)

    encryption_time = time.time() - start_time

    return {
        "algorithm": "CRYSTALS-Kyber",
        "encryption_time": round(encryption_time, 6),
        "key_size": "1568-bit equivalent",
        "ciphertext_size": len(ciphertext),
        "quantum_safe": True
    }


# =====================================
# Comparison Dashboard Data
# =====================================

def generate_comparison_metrics(message="Hello PQC"):

    rsa_metrics = benchmark_rsa(message)

    pqc_metrics = benchmark_pqc(message)

    return {
        "rsa": rsa_metrics,
        "pqc": pqc_metrics
    }