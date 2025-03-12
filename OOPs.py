class employee:
    
    def __init__(self):
        self.id = 123
        self.name = "abc"
        self.salary = 50000
        self.designation = "SDE"
        print("init method is working")
        
    def travel(self, destination):
        print(f"This vacation destination might be {destination}")
        
tony = employee()

            