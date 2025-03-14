class chatbook:
    
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()
        
        
    def menu(self):
        print(""" This is the menu to choose from:
              Pick a number for the desired operation
              1. To signup
              2. To signin
              3. To post something
              4. To send a message to a friend
              5. To end the menu""")
        
        option = input("Enter the number to choose the operation-> ")
        
        if option == "1":
            self.signup()
        elif option == "2":
            self.signin()
        elif option == "3":
            self.post()
        elif option == "4":
            pass
        else:
            exit()
        
    def signup(self):
        print("Enter the signup details below")
        username = input("Enter your username-> ")
        pswd = input("Enter password-> ")
        self.password = pswd
        self.username = username
        print("Signup successfull!")
        self.menu()
        
    def signin(self):
        if (self.username == "") and (self.password == ""):
            print("Signup first")
            self.signup()
        else:
            print("Enter the signin details below")
            username = input("Enter the username-> ")
            pswd = input("Enter the password-> ")
            if self.username == username and self.password == pswd:
                print("Signin successfull!")
                self.loggedin = True
                self.menu()          
            else:
                print("Enter the password correctly")
                self.signin()
                
    def post(self):
        if self.loggedin == True:
            print("Enter the post below")
            post = input("")
            print(f"This is your post {post}")
            self.menu()
        else:
            self.signin()
    
chat = chatbook()

