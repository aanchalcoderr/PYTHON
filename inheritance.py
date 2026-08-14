#way to show inherited class of superclass


class Human:
    def work(self):
        print("all humans can work")
    def eat(self):
        print("all humans can eat")
class Male(Human):         # way to show inherited class of human
                           #inherited class can have its own methods too
     def sex(self):
         print("i am male")
     def work(self):
         super().work()   #aise ham superclass ka bhi method use kr skte
         print("all males can work")
male_1=Male()
male_1.work()
male_1.eat()
male_1.sex()

#male_1.eat()

                          #derived class can have its own implementation of methods that are in super class-----overridding







#how to use super class init 
#uske liye tumko  derived class ke init mein super().init () likh ke jo bhi uske parameters hai usko pass kr dena hai

class Subject:
    def __init__(self,name):
        self.name=name
        print(self.name)
        print("i am superclass init")


class Python(Subject):
    def __init__(self,marks, name):   # parameters ke order se koi frk nhi padta 
        super().__init__(name)
        self.marks=marks
        print("i am subclass init")
    def display(self):
        print(self.marks)

subj1=Python(23,"python")
subj1.display()
