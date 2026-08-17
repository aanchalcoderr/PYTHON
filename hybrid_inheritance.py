#mixture of two or more inheritance


class A:

    def display(Self):
            print("class A")

class B:
    def display(Self):
        print("class B")

class C(A,B):
     
     def display(Self):
             print("class C")
class D:
     def display(self):
          A.display(self)
          B.display(self)
          C.display(self)
          print("class D")
      
d1=D()
d1.display()