#tp print uppercase then lowercase in a string


'''
str=input("input string: ")
upcs=""
lpcs=""
for i in str:
    if i>="A" and i<="Z":
        upcs+=i
    else:
        lpcs+=i
print(upcs+lpcs)'''




#to find whether two strings are balanced or not

'''
str=input("enter string: ")
str2=input("enter string: ")
flag=0
for i in str2:
    if i not in str:
        flag=1

if(flag ==1):
    print("not balanced")
else:
    print("balanced")'''



#to count vowels and print it

s = input("Input string: ")
vow = "aeiouAEIOU"
count = {}

for i in s:
    if i in vow:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

for i in count:
    print(i, ":", count[i])
    