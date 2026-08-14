class Instructor:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def display(self):
        print("hello")
    def occupation(self,occupation):
          print(occupation)  #if it was attribute of object it must be self.  otherwise its just in parameter of funciton we cn write it directly
ins1=Instructor("aanchal","delhi")
print(ins1.name)
print(ins1.address)
print(ins1.display())   #object ke saath function ko link krna hota hai
#                        dekho print statement kya print karega jo function retuen karega but display function toh kuch return hi nhi kr rha wo toh ba print kr rha
ins1.occupation("teacher")




#to print area and perimeter  of square using oops

class Area:
    def __init__(self,side):
          self.side=side
    def calc(self):
          print(f"{self.side}*{self.side}=",self.side*self.side)
    def peri(self):
         print(4*self.side)   
square=Area(2)
square.calc()
square.peri()
