from cryptography.fernet import Fernet
key=Fernet.generate_key()
f=Fernet(key)
message=b"hello how are you i am under the water wuwuwuw"
'''the encryption key generated here is used make the encryption secure if any
one gets the key then they can decrypt our cipher text '''

fftoken=f.encrypt(message)
print(fftoken)
print()
d=f.decrypt(fftoken)
print(d.decode("utf-8"))