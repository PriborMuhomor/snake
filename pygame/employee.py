class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position
    def __str__(self):
         return(f"Name: {self.name}, Position: {self.position}")
        

class Controller:
    def __init__(self):
        self.employees = {}

        
        
    def show_list(self):
        for name in self.employees.keys():
            
            print(self.employees[name])
        print(" ")
    def add_employee(self, name, position):
        self.employees[name] = Employee(name,position)

    def remove_employee(self, name):
        if name in self.employees.keys():
            del self.employees[name]

    
controller = Controller()
controller.add_employee("William", "HR")
controller.show_list()
controller.add_employee("Bob","intern")
controller.show_list()
controller.remove_employee("Bob")
controller.show_list()
