class Instructor:
    pass
Instructor_1=Instructor()
                           # we can also assign values like 
Instructor_1.name="Chotu"
Instructor_1.address="Delhi"
Instructor_2=Instructor()
Instructor_2.name="Shri Ram"
Instructor_2.address="Kerela"
                        #here yaha pe kevl name isliye nhi likhte kyuki name is only variable but instructor_!.name attribute associated with object hai
                        #aise bhi likh skte hai but kya pata koi instructor_2.insname naam rkh de attribute ka phir  isiliye class ka use
                        #hoga aur init function ka..... wo apne aap kaam karega jb bhi koi object banega usme parameters phle se honge bs ussi hisab 
                        # se object banate waqt values daal dena  lines of codes bhi kam ho jaenge self ek keyword hoga jab wo koi bhi object banega phir self usko replace kardega .......


class Instructor:
    def __init__(self,name,address):
        self.name=name
        self.address=address

ins_1=Instructor("Aanchal","Delhi")
print(ins_1.name)
print(ins_1.address)
ins_2=Instructor("Chotu","HP")
print(ins_2.name)
print(ins_2.address)


#to set defalut values


class Instructor:
    def __init__(self,name,address):   # agr yaha pe parameter mein daal de followers to sabko likhna follower count bhi compulsory ho jaega see next example
        self.name=name
        self.address=address
        self.followers=0       #matlab default followers 0 hoga agr koi nhi daala toh ya kisi ka zero hai to usko likhne ki jarrorat nhi hai
        
ins_1=Instructor("Aanchal","Delhi")
print(ins_1.name)
print(ins_1.address)
print(ins_1.followers)
ins_2=Instructor("Chotu","HP")
print(ins_2.name)
print(ins_2.address)




class Instructor:
    def __init__(self,name,address,follower): 
        self.name=name  
        self.address=address
        #self.followers=0                             # agr ye likha hai matlb ham koi bhi value daale 0 hi hoga kyuki wo usse link hi nhi hai 
        self.followers=follower                             # follower aur self.followers    
        
ins_1=Instructor("Aanchal","Delhi",5)
print(ins_1.name)
print(ins_1.address)
print(ins_1.followers)
ins_2=Instructor("Chotu","HP",7)
print(ins_2.name)
print(ins_2.address)
print(ins_2.followers)

