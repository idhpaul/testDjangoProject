from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

from my_settings import MY_SECRET


private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

pem = private_key.private_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PrivateFormat.PKCS8,
   encryption_algorithm=serialization.BestAvailableEncryption(bytes(MY_SECRET['SECRET_KEY'],'utf-8'))
)

print(pem.splitlines()[1])

public_key = private_key.public_key()
pempub = public_key.public_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print(pempub.splitlines()[1])