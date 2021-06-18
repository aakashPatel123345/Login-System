grant = False
def grant():
    global granted
    granted = True



def login(username, password):
    success = False
    file = open("user_details.txt","a")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if(username == a and password == b):
            success = True
            break
    file.close()
    if(success):
        print("Login Successful")
        grant()
    else:
        print("Login Failed: Wrong Username or Password")


            

def register(username, password):
    file = open("user_details.txt","a")
    file.write("\n"+username+","+password)
    file.close()
    grant()

def begin():
    global option
    print("Aakash's First Python Project: Welcome!")
    option = input("Login or Register (L or R) ")
    if(option!="L" and option!="R"):
        begin()

def access(option):
    global username
    if(option == "L"):
        username = input("Enter your username:")
        password = input("Enter your password: ")
        login(username,password)
    else:
        print("Enter your username and password to register")
        username = input("Enter your username")
        password = input("Enter your password")
        register(username,password)


    

begin()
access(option)
if(grant):
    print("Welcome to this website")
    print("### User Details ####")
    print("Username: ",username)
