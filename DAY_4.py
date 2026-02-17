# ATM PIN SYSTEM
pin=int(input("Enter the pin: "))
count=0
while count<2:
    if pin==1234:
        print("Acess granted")
        break
    else:
        count+=1
        print("Invalid pin")
        pin=int(input("Enter the pin again: "))
if count==2:
    print("Card is blocked")

# SUM UNTIL ZERO
num=int(input("Enter a number: "))
total=0
while not num==0:
    total+=num
    num=int(input("Enter a number: "))
print("The total: ",total)

# SIMPLE GREETING FUNCTION
def greet(name):
    print(f"Hello {name} ,welcome")
greet("Angela")

# SQUARE OF A NUMBER
def squre(num):
    s=num*num
    return(s)
print(squre(6))

# EVEN OR ODD CHECKER
def check_even_odd(num):
    if num%2==0:
        z="even"
        return(z)
    else:
        z="odd"
        return(z)
print(check_even_odd(5))

# MAXIMUM OF THREE NUMBERS
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))
def find_max(a,b,c):
    if a>b and a>c:
        print(f"{a} is the largest")
    elif b>c:
        print(f"{b} is the largest")
    else:
        print(f"{c} is the largest")
find_max(n1,n2,n3)