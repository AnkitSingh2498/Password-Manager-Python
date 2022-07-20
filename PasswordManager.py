from cryptography.fernet import Fernet


'''
def write_key():
    key = Fernet.generate_key()
    with open ("key.key","wb") as key_file:
        key_file.write(key)'''
def load_key():
    file=open("key.key","rb")
    key=file.read()
    file.close()
    return key

master_pwd=input("What is the Master Password ? ")
key=load_key() + master_pwd.encode()
fer=Fernet(key)

def view():
    with open('passwords.txt','r') as f:  # with keyword is used to open file with different modes but it automatically closes file after completing its task
        for line in f.readlines():
            data=line.rstrip()
            user,passw=data.split("|")
            print("User: ",user,"\n", "Password: ",fer.decrypt(passw.encode()).decode())

def add():
    name=input("Account name: ")
    pwd =input("password: ")

    with open('passwords.txt','a') as f:  #with keyword is used to open file with different modes but it automatically closes file after completing its task
        f.write(name +"|"+fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode=input("Would you like to View the existing Password or Add a new password (view,add), press q to quit? ").lower()
    if mode=="q":
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Invalid Input")
        continue