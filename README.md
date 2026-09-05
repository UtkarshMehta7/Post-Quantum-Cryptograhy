# Post-Quantum Cryptography (PQC)

An interactive security platform exploring the impact of quantum computing on
classical cryptography and the transition toward Post-Quantum Cryptography (PQC).

The project demonstrates classical RSA cryptography, post-quantum cryptographic
concepts, quantum attack scenarios, hybrid migration strategies, and comparisons
between classical and post-quantum approaches.

---

## Overview

Quantum computing introduces new security challenges for widely used
public-key cryptographic algorithms such as RSA and ECC.

This project explores these challenges through an interactive web-based platform
and supporting cryptographic demonstrations.

It focuses on:

- Quantum threats to classical cryptography
- Shor's algorithm and its impact on RSA/ECC
- Post-Quantum Cryptography (PQC)
- ML-KEM (Kyber) concepts
- ML-DSA (Dilithium) concepts
- Hybrid cryptographic migration
- Classical vs. post-quantum comparisons
- Lattice-based cryptography
- Quantum attack simulations

---

## Key Features

### 🔐 RSA Cryptography

- RSA-2048 encryption and decryption demonstration
- Classical public-key cryptography analysis
- Demonstration of the security challenges posed by future quantum computers

### 🛡️ Post-Quantum Cryptography

- Exploration of ML-KEM (Kyber)
- Exploration of ML-DSA (Dilithium)
- Post-quantum key establishment concepts
- Post-quantum digital signature concepts
- Lattice-based cryptography concepts

### ⚛️ Quantum Threat Simulation

- Visualization of quantum threats
- Shor's algorithm concepts
- RSA/ECC vulnerability analysis
- Quantum attack scenarios

### 🔄 Hybrid Migration

- Classical + PQC migration strategy
- Analysis of cryptographic transition requirements
- Enterprise-oriented PQC migration concepts

### 📊 Cryptographic Comparison

- Classical RSA vs. PQC comparison
- Algorithm characteristics
- Security and migration considerations
- Interactive cryptographic demonstrations

---

## Technology Stack

### Backend

- Python
- Flask
- Flask-CORS
- NumPy
- PyCryptodome
- Gunicorn
- REST APIs

### Frontend

- HTML5
- CSS3
- JavaScript

### Java Module

- Java
- Object-Oriented Programming
- Java Cryptography APIs
- SHA-256
- PQC algorithm demonstrations and analysis

The `PQCJavaDemo.java` file provides a standalone Java-based cryptography
demonstration related to the project's PQC concepts.

---

## Project Structure

```text
Post-Quantum-Cryptography/
│
├── README.md
│
├── app.py
├── comparison_engine.py
├── pqc_demo.py
├── rsa_demo.py
├── test_oqs.py
├── requirements.txt
│
└── PQCJavaDemo.java