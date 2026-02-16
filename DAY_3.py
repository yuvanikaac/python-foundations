# STUDENT GRADE LOOKUP (DICTIONARY)
grades={"Ram":"A","Sita":"B","Arun":"A+","Kiran":"C"}
g=input("Enter student name: ")
if g in grades:
    print(f"The grade of {g} is {grades.get(g)}")
else:
    print(f"No student found with the name {g}")

# UPDATE MARKS (DICTIONARY)
marks={"Priya":85,"Roshini":92,"Arjun":68}
n=input("Enter the name of the student whose marks has to be updated: ")
m=int(input(f"Enter the marks to be updated for {n}: "))
n_mark=marks.update({n:m})
print("the updated dictionary is: ",marks)

#SIMPLE PRODUCT INVENTORY
products={"Pen":10,"Pencil":6,"Scale":15,"Eraser":8}
p=input("Enter your required product: ")
if p in products:
    print(f"The price of {p} is {products.get(p)}")
else:
    print(f"{p} is not available")

