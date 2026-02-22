print("======WELCOME TO OUR CLI CALCULATOR======")
print("MENU")
print("1.Addition\n""2.Subtraction\n""3.Multiplication\n""4.Division\n""5.Power\n""6.Exit")
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    if n2==0:
        return "Division is not possible"
    else:
        return n1/n2
def power(n1,n2):
    return n1**n2
        
while True:
    c=int(input("Enter your choice: "))
  
    if c==1:
        n1=int(input("Enter the first number: "))
        n2=int(input("Enter the second number: "))
        print(f"The sum of {n1} and {n2} is:{add(n1,n2)}")
    elif c==2:
        
        n1=int(input("Enter the first number: "))
        n2=int(input("Enter the second number: "))
        if n1>n2:
            print(f"The difference of {n1} and {n2} is:{sub(n1,n2)}")
        else:
            print(f"The difference of {n2} and {n1} is:{sub(n2,n1)}")
    elif c==3:
        n1=int(input("Enter the first number: "))
        n2=int(input("Enter the second number: "))
        print(f"The product of {n1} and {n2} is:{mul(n1,n2)}")
    elif c==4:
        n1=int(input("Enter the first number: "))
        n2=int(input("Enter the second number: "))
        if n2==0:
            print("Division is not possible")
        else:
            
            print(f"The quotient of {n1} and {n2} is:{div(n1,n2)}")
    elif c==5:
        n1=int(input("Enter the base number: "))
        n2=int(input("Enter the power number: "))
        print(f"{n1} to the power of {n2} is: {power(n1,n2)}")
    elif c==6:
        print("Thank you for using our calculator")
        break
    else:
        print("Invalid input,please choose the choice from the menu")
       
