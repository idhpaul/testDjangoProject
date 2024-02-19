from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

from my_settings import MY_SECRET

with open("rsa_2048.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=bytes(MY_SECRET['SECRET_KEY'],'utf-8'),
    )

    

public_key = private_key.public_key()
pempub = public_key.public_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print(pempub)