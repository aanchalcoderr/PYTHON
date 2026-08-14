class Human:
    def __init__(self):
        self.numnose=2
        print("main class init called")
    def work(self):
        print("all humans can work")
class Man:
    def __init__(self,name):
      
      self.name=name
      print("subclass int called")
    def work (self):
        print("all mn can work")

class Boy(Human,Man):
    def __init__(self,name):   #without this init of main class is called aotomatically lekin agr init sub class ka chahiye toh
        Man.__init__(self,name)
    def work(self):
        print("all boys can work")

child1=Boy("g")
child1.work()
Man.work(child1)   # in order to get particular method of particular class
 #if all classes have the method with same name it will go first in derived then in the 
 #classes mention order in bracket like human then male order can be reversed also according to needs but lets see other ways too
#child class ke pass agr apna init hai toh khud ke parameters ke saath saathupper classes ke bhi parametrs likhne honge
