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
            pass
        elif option == "3":
            pass
        elif option == "4":
            pass
        else:
            exit()
        
    def signup(self):
        username = input("Enter your username")
        pswd = input("Enter password")
        print("Signup successfull!")
        self.menu()
                
chat = chatbook()

