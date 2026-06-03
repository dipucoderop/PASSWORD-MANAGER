
from cryptography.fernet import Fernet
key69=Fernet.generate_key()
with open("key.key", "ab+") as po:
    po.write(key69)

# load previously saved key (binary)
with open("key.key", "ab+") as kf:
    key = kf.read()

jp = Fernet(key)

with open("masterpassw.txt", "r") as ff:
    j = ff.readline().strip()       # read first line and strip newline

# decrypt expects bytes
p = jp.decrypt(j.encode()).decode()

print("master password:", p)