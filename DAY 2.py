# STUDENT MARKS ANALYZER(LIST)
marks=[45,89,55,72,25]
avg=sum(marks)/len(marks)
print(f"The average mark obtained is:{avg}")
print(f"The highest mark obtained is:{max(marks)}")
print(f"The lowest mark obtained is:{min(marks)}")

# REMOVE DUPLICATE NAMES(SET)
names=["Ram","Sita","Ram","Krishna","Sita"]
print("The list of names are:",names)
names=set(names)
print("The uniques names are:",names)
print("The number of uniques names are: ",len(names))

# SHOPPING CART (LIST)
cart=[]
item_1=input("Enter the first item : ")
item_2=input("Enter the second item: ")
item_3=input("Enter the third item: ")
cart.append(item_1)
cart.append(item_2)
cart.append(item_3)
print("The items in the cart are:",cart)

#TUPLE INFORMATION DISPLAY
t=("Ram",21,"Chennai")
print("Name: ",t[0])
print("Age: ",t[1])
print("City: ",t[2])
print("The length of the tuple is: ",len(t))

# COMMON SUBJECTS (SET OPERATIONS)
s1={"Maths","Physics","Chemistry"}
s2={"Biology","Physics","Chemistry"}
print("The common subjects for both the students are: ",s1.intersection(s2))
print("All the subjects are: ",s1.union(s2))
print("Subjects only for the first student is: ",s1.difference(s2))