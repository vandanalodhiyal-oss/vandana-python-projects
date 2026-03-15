name = input("Enter your name: ")
age = int(input("Enter your age: "))   # age normally integer hota hai
degree = input("Enter your degree: ")

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))


subjects = ["Subject 1", "Subject 2", "Subject 3"]

marks = {
    "Subject 1": m1,
    "Subject 2": m2,
    "Subject 3": m3
}

skills = {"Python", "Communication", "Python"}


total = m1 + m2 + m3
percentage = total / 3



print("Name:", name)
print("Age:", age)
print("Degree:", degree)
print("Subjects:", subjects)
print("Marks:", marks)
print("Skills:", skills)
print("Percentage:", percentage)


if age >= 18 and degree == "BSc" and percentage >= 75:
    print("\nStatus: Eligible for Admission")
    print("Grade: A")
elif age >= 18 and percentage >= 60:
    print("\nStatus: Eligible with Counseling")
    print("Grade: B")
elif age >= 18 and percentage >= 50:
    print("\nStatus: Average Candidate")
    print("Grade: C")
else:
    print("\nStatus: Not Eligible")