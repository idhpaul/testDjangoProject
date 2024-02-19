import base64
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from my_settings import MY_SECRET


with open("./rsa_2048.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=bytes(MY_SECRET['SECRET_KEY'],'utf-8'),
    )
        
public_key = private_key.public_key()
pem = public_key.public_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo
)
    
print(pem)
        
text = b'{\'email\':\'foo@foo.com\'}'

# plain to chiper (pubENC(text))
ciphertext = public_key.encrypt(
    text,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

ciphertext_enc_base64 = base64.urlsafe_b64encode(ciphertext)
print(ciphertext_enc_base64)


ciphertext = base64.urlsafe_b64decode(ciphertext_enc_base64)
print(ciphertext)


# chiper to plain(priDEC(pubENC(plain_text)))
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(plaintext)
plaintext == ciphertext