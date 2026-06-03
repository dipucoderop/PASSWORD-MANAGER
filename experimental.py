from cryptography.fernet import Fernet
key69=Fernet.generate_key()
jp=Fernet(key69)
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
    h=ff.readlines()
    j=h[0]
    p=jp.decrypt(j).decode()
ff.close()
if A==p:
   key=Fernet.generate_key()
   fo=Fernet(key)

   def view():
    with open("password.txt", "r") as fp:
        h=fp.readlines()
        for line in h:
            website, username, encrypted = line.strip().split("|")
            password = fo.decrypt(encrypted.encode()).decode()
            print(website,username,password)

   def add():
    
    with open("password.txt","a+") as pf:
        username=input("ENTER YOUR USERNAME:")
        password=input("ENTER PASSWORD:")
        website=input("ENTER IN WHICH WEBSITE YOU HAVE THAT ACCOUNT:")
        pf.write(website+"|"+username+"|"+fo.encrypt(password.encode()).decode()+"\n")
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