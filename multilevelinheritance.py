class Human(object):  # object is like parent class of all classes like if u mention or not it is the parent class of all classes

    def __init__(self):
       print("hello")
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class Male(Human):
    def __init__(self,name):
        self.name=name
        print("calling name from male class")
    def sleep(self):
        print("i can sleep whole day")
class Boy(Male):
    def work(self):
        Human.__init__(self)
        print("all boys can work")
    
boy1=Boy("ajay")
boy1.work()

