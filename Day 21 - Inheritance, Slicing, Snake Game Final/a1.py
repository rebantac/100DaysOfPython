from calendar import c


class Employee:


    def __init__(self):
        self.id = 1

    
    def work(self):
        print("Employee is working.")



class Manager(Employee):


    def __init__(self):
        super().__init__()
    

    def work(self):
        super().work()
        print("Employee is managing")


tom = Manager()
tom.work()
print(tom.id)
    