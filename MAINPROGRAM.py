from cryptography.fernet import Fernet
s=str(input("IF YOU ARE NEW CREATE maximum 15 character MASTERPASSWORD BY PRESSING D AND IF ALREADY CREATED EARLIER THEN PRESS F"))
if s=="D":
   
  with open("masterpassw.txt","a+") as pp:
     l=input("ENTER YOUR MASTER PASSWORD")
     if len(l)==15:
        print("SO YOUR MASTER PASSWORD IS:",l)
        print("ALWAYS REMEBER THIS MASTERPASSWORD IN ORDER TO ACCESS YOUR PASSWORDS")
        pp.write(l)
     else:
        print("ENTER 15 CHARACTER MASTERPASSWORD")
     

A=str(input("Enter your Master password"))
with open("masterpassw.txt","r") as ff:
    s=ff.readlines()
    j=s[0]
ff.close()
if A==j:
   import os

   def write_key():
       key = Fernet.generate_key()
       with open("key.key", "wb") as key_file:
           key_file.write(key)

   def load_key():
       with open("key.key", "rb") as file:
           return file.read()

   if not os.path.exists("key.key"):
       write_key()

   key = load_key()
   h = Fernet(key)

   def view():
    with open("password.txt", "r") as fp:
        L=fp.readlines()
        for line in L:
            website, username, encrypted = line.strip().split("|")
            password = h.decrypt(encrypted.encode()).decode()
            print(website,username,password)

   def add():
    
    with open("password.txt","a+") as pf:
        username=input("ENTER YOUR USERNAME:")
        password=input("ENTER PASSWORD:")
        website=input("ENTER IN WHICH WEBSITE YOU HAVE THAT ACCOUNT:")
        pf.write(website+"|"+username+"|"+ (h.encrypt(password.encode())).decode()+"\n")
    pf.close()
   while True:
    mode=input("PRESS 1 TO VIEW PASSWORD,PRESS 2 TO ADD PASSWORD,PRESS Q TO QUITE")
    if mode=="1":
          view()
          continue
    if mode=="2":
          add()
          continue
    if mode=="q":
         break  
else:
   print("PLEASE ENTER VALID MASTERPASSWORD!!")