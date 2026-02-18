# PRINT NUMBERS 1 TO N
n=int(input("Enter a number: "))
for n in range(1 ,n+1):
    print(n)

# MULTIPLICATION TABLE
num=int(input("Enter the table: "))
for i in range(1,10+1):
    print(num,"*",i,"=",num*i)             

# SUM OF FIRST N NUMBERS
numb=int(input("Enter the range: "))
start=0
for i in range(1,numb+1):
    start+=i
print(start)

# COUNT VOWELS
def count_vowels(t):
    count = 0
    for i in t:
        if i in "aeiou":
            count += 1
    print("The count of vowels is:", count)

t = input("Enter the word: ")
count_vowels(t)


# ADDITION
num=int(input("Enter the table: "))
for i in range(1,10+1):
    print(num,"+",i,"=",num+i)
    