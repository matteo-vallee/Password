import hashlib
import json




try:
    with open("storage.json", "r") as f:
        storage = json.load(f)
except json.decoder.JSONDecodeError as e:
    print(f"Error: {e}")
    storage = {}

def condPasswordlen(take):
   if len(take) >= 8 :
       return True
def condPasswordMaj(take):
    for char in take :
        if char.isupper():
            return True
def conPasswordMin(take):
    for char in take:
        if char.islower():
            return True
def conPasswordSpe(take):
    for char in take:
        if char in ";/.?§%£$!:,(-_)=/*-+#[|`@]}":
            return True
def conPasswordNum(take):
    for char in take:
        if char in "1234567890":
            return True



def Passwordprog():
    global storage
    comp = None
    new = "yes"
    data = None
    while True:
        if new == 'yes':
            print("choose a username")
            username = input()
            print("choose a password")
            password = input()
        if conPasswordNum(password) and conPasswordMin(password) and condPasswordMaj(password) and conPasswordSpe(password) and condPasswordlen(password):
            print("Valid password")
            stored_password = storage.get(username)
            if not stored_password:
                print("Username not found.")
                password_encoded = hashlib.sha256(password.encode()).hexdigest()
                storage[username] = password_encoded
                with open("storage.json", "a") as f:
                    json.dump(storage, f)
                print('do you want to see the password store(yes or no) :')
                data = input()
                if data == "yes":
                    print(storage)
                print('do you want to put a new password ?(yes or no)')
                new = input()
                if new == 'no':
                    print("goodbye")
                    break
            if stored_password == password_encoded:
                print("Password already existed.")
        else:
            print("your password is invalid")
Passwordprog()
