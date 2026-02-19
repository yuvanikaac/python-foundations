print("======WELCOME TO OUR CLI CALCULATOR======")
print("MENU")
print("1.Addition\n""2.Subtraction\n""3.Multiplication\n""4.Division\n""5.Exit")
while True:
    c=int(input("Enter your choice: "))
    if c==1:
        n1=int(input("Enter the first number: "))
        n2=int(input("Enter the second number: "))
        print(f"The sum of {n1} and {n2} is:{n1+n2}")
    elif c==2:
        n1=int(input("Enter the first number: "))
        n2=int(input("Enter the second number: "))
        print(f"The difference of {n1} and {n2} is:{n1-n2}")
    elif c==3:
        n1=int(input("Enter the first number: "))
        n2=int(input("Enter the second number: "))
        print(f"The product of {n1} and {n2} is:{n1*n2}")
    elif c==4:
        if n2==0:
            print("Division is not possible")
        else:
            n1=int(input("Enter the first number: "))
            n2=int(input("Enter the second number: "))
            print(f"The quotient of {n1} and {n2} is:{n1/n2}")
    elif c==5:
        print("Thank you for using our calculator")
        break
    else:
        print("Invalid input,please choose the choice from the menu")
       
