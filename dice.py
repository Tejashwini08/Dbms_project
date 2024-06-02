import random
s=random.randint(1,6)
print("your die number is : ",s)
r=int(input("type zero or one : "))
print("u have entered : ",r)

b=0

while r>0:

    
        print("u can roll the again")
        print(random.randint(1,6))
        r=int(input("type 0 or 1 : "))
        print("u have entered : ",r)
        

else:
      print("no need of rollig a die")
