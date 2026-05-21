
try:
    import oqs

    print("====================================")
    print("Open Quantum Safe Test")
    print("====================================")

    print("\nInstalled OQS Module Loaded Successfully")

    print("\nAvailable Attributes Inside oqs Module:\n")

    available_items = dir(oqs)

    for item in available_items:
        print("-", item)

    print("\n====================================")
    print("Environment Check Complete")
    print("====================================")

    # =====================================
    # Check if KeyEncapsulation Exists
    # =====================================

    if hasattr(oqs, "KeyEncapsulation"):

        print("\nKeyEncapsulation API Found")
        print("\nTesting ML-KEM-512...\n")

        kemalg = "ML-KEM-512"

        with oqs.KeyEncapsulation(kemalg) as server:

            public_key = server.generate_keypair()

            with oqs.KeyEncapsulation(kemalg) as client:

                ciphertext, shared_secret_client = client.encap_secret(public_key)

            shared_secret_server = server.decap_secret(ciphertext)

        print("Algorithm:", kemalg)
        print("Public Key Size:", len(public_key), "bytes")
        print("Ciphertext Size:", len(ciphertext), "bytes")
        print("Shared Secret Size:", len(shared_secret_client), "bytes")

        print("\nShared Secret Match:")
        print(shared_secret_client == shared_secret_server)

        print("\n====================================")
        print("Real PQC Environment Working")
        print("====================================")

    else:

        print("\nKeyEncapsulation API NOT FOUND")
        print("\nThis means the installed oqs package is incorrect")
        print("or liboqs-python bindings are missing.")

except Exception as error:

    print("\n====================================")
    print("OQS TEST FAILED")
    print("====================================")

    print("\nError Details:\n")
    print(error)
