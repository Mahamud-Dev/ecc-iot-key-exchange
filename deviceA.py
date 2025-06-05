from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec



# Load Device A's private key
with open("device_a_private.pem" , "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

# Load Device B's public key
with open("device_b_public.pem" , "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Derive the shared key
shared_key_a = private_key.exchange(ec.ECDH() , public_key)

print("Device A Shared Key:", shared_key_a.hex())




