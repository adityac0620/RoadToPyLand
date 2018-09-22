import math
print("Let's get the fest started")
a=eval(input("Enter a number : "))
b=eval(input("Enter another number : "))

# Basic Arithmetic Operations
print(a,"+",b,"=",a+b)
print(a,"-",b,"=",a-b)
print(a,"*",b,"=",a*b)
print(a,"/",b,"=",a/b)
print(a,"%",b,"=",a%b)
print(a,"**",b,"=",a**b)

# To find the Greatest among the two numbers 
if a<b :
    print(a,"<",b)
elif a>b:
    print(a,">",b)
else:
    print(a,"=",b)

# To print "a", "b" number of times
for i in range(b) :
    print(a,"",end="\n")

# To create and display a list of (a*b) Fibonacci Numbers
fino=[0,1]
for i in range(a*b):
    x=fino[-1]+fino[-2]
    fino.append(x)
print(fino)
