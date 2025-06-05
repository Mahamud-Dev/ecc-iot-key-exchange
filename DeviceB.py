from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec



#5. Load Device B's private key
with open("device_b_private.pem" , "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

#6. Load Device A's public key
with open("device_a_public.pem" , "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

#7. Derive the shared key
shared_key_b = private_key.exchange(ec.ECDH() , public_key)

print("Device B Shared Key:", shared_key_b.hex())

