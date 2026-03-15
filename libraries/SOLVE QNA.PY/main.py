name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))


print("Name:", name)
print("Age:", age)
print("Marks:", marks)

if age >= 18 and marks >= 90:
    print("Status: Eligible")
    print("Grade: A")
elif age >= 18 and marks >= 70:
    print("Status: Eligible")
    print("Grade: B")
elif age >= 18 and marks >= 50:
    print("Status: Eligible")
    print("Grade: C")
else:
    print("Status: Not Eligible")
