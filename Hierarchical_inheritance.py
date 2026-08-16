#Hierarchical Inheritance
#Hierarchical inheritance means multiple child classes inherit from the same parent class.
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("calling init from human class")
    def eat(self):
        print(" i can eat")
    def display(self):
            print(f'{self.name},{self.age}')
class Male(Human):
    def sleep(self):
        print("i can sleep whole day")
        
class Female(Human):
    def __init__(self, name, age):
        super().__init__(name, age)   #no need to pass self.... just parameters only
    def work(self):
        print("i can code")
    def show_details(self):
        Human.display(self)
female1=Female("aanchal",19)
female1.eat()
female1.work()
female1.show_details()
#female1.sleep()   # cuz theres no reln between male and female class so it cant access its method
male1=Male("ajay",23)
male1.sleep()
male1.display()

