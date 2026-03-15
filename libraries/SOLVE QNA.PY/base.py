name = "Vandana"
age = 21
course = "Python Programming"
is_student = True

print("Student Name:", name)
print("Age:", age)
print("Course:", course)
print("Is Student:", is_student)

#List 

subjects = ["Math", "Physics", "Chemistry"]
print("Subjects enrolled:", subjects)

#Tuple 

grades = (85, 90, 95)
print("Grades obtained:", grades)

#Set 

skills = {"Python", "HTML", "CSS"}
print("Skills:", skills)
 
#Dictionary

marks = {"Math":85, "Physics":90, "Chemistry":95}
print("Marks:", marks)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
   result: float = num1 + num2

elif operation == "-":
   result = num1 - num2

elif operation == "*":
   result = num1 * num2

elif operation == "/":
   result = num1 / num2

print("Result:", result)

