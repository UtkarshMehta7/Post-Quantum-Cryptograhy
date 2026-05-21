from flask import Flask, jsonify, request
import datetime
from flask_cors import CORS
from rsa_demo import generate_rsa_demo
from pqc_demo import generate_pqc_demo

app = Flask(__name__)
CORS(app)

# =====================================
# Home Route
# =====================================

@app.route('/')
def home():
    return jsonify({
        "message": "Post-Quantum Cryptography Backend Running",
        "status": "ACTIVE",
        "timestamp": str(datetime.datetime.now()),
        "services": {
            "rsa": "ACTIVE",
            "pqc": "ACTIVE",
            "hybrid": "ACTIVE"
        }
    })

# =====================================
# RSA Demonstration Route
# =====================================

@app.route('/rsa-demo', methods=['POST'])
def rsa_demo():

    data = request.get_json()

    message = data.get('message', '')

    try:

        rsa_result = generate_rsa_demo(message)

        return jsonify(rsa_result)

    except Exception as error:

        return jsonify({
            "algorithm": "RSA",
            "status": "FAILED",
            "error": str(error)
        }), 500

# =====================================
# PQC Demonstration Route
# =====================================

@app.route('/pqc-demo', methods=['POST'])
def pqc_demo():

    data = request.get_json()

    message = data.get('message', '')

    try:

        pqc_result = generate_pqc_demo(message)

        return jsonify(pqc_result)

    except Exception as error:

        return jsonify({
            "algorithm": "ML-KEM-512",
            "status": "FAILED",
            "error": str(error)
        }), 500

# =====================================
# Hybrid Migration Route
# =====================================

@app.route('/hybrid-status')
def hybrid_status():

    return jsonify({
        "phase_1": "Classical Cryptography",
        "phase_2": "Hybrid Cryptography",
        "phase_3": "Quantum-Safe Infrastructure",
        "nist_status": "ML-KEM Standardized",
        "migration_status": "In Progress",
        "quantum_threat": "Increasing"
    })

# =====================================
# Quantum Attack Simulation Route
# =====================================

@app.route('/quantum-attack')
def quantum_attack():

    return jsonify({
        "rsa_attack": {
            "algorithm": "Shor's Algorithm",
            "target": "RSA",
            "status": "VULNERABLE",
            "steps": [
                "Quantum Period Finding Initialized",
                "Large Integer Factorization Started",
                "Prime Factors Recovered",
                "RSA Private Key Derived",
                "RSA Encryption Broken"
            ]
        },

        "pqc_attack": {
            "algorithm": "Quantum Lattice Attack",
            "target": "ML-KEM / CRYSTALS-Kyber",
            "status": "RESISTANT",
            "steps": [
                "Lattice Reduction Attempted",
                "Noisy Polynomial Vectors Encountered",
                "Learning With Errors Problem Generated",
                "Quantum Complexity Increased",
                "No Efficient Quantum Attack Known"
            ]
        },

        "comparison": {
            "rsa_security": "Integer Factorization",
            "pqc_security": "Lattice Hardness + Noise",
            "quantum_risk": "RSA High Risk",
            "pqc_quantum_status": "Quantum Resistant"
        }
    })

# =====================================
# Lattice Cryptography Explanation Route
# =====================================

@app.route('/lattice-info')
def lattice_info():

    return jsonify({
        "concept": "Lattice-Based Cryptography",
        "description": (
            "Post-Quantum Cryptography uses multidimensional lattice "
            "mathematics, polynomial rings, modular arithmetic, and "
            "noise distributions to resist quantum attacks."
        ),

        "core_components": {
            "matrix_A": "Public random matrix",
            "secret_vector_s": "Hidden secret vector",
            "noise_e": "Random error/noise term",
            "modulus_q": "Finite modular arithmetic field"
        },

        "lwe_problem": {
            "name": "Learning With Errors",
            "difficulty": "Extremely Hard",
            "quantum_status": "No Practical Quantum Solution Known"
        },

        "advantages": [
            "Quantum Resistant",
            "Fast Key Exchange",
            "NIST Standardized",
            "Suitable For Future Internet Security"
        ]
    })

# =====================================
# Start Server
# =====================================

if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )