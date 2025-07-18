from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec


# 2. Derive the public key from the private key
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

# 3. Serialize and save the private key to PEM
with open("device_b_private.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()  # Optional: use a password-based encryption algorithm here if needed
    ))

# 4. Serialize and save the public key to PEM
with open("device_b_public.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))