print("---------- RESUME ----------")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
degree = input("Enter your degree: ")
percentage = int(input("Enter your percentage: "))

print("\n---------- YOUR RESUME ----------")
print("Name:", name)
print("Age:", age)
print("Degree:", degree)
print("Percentage:", percentage)

if percentage >= 75:
    print("Status: Excellent Candidate")
elif percentage >= 60:
    print("Status: Good Candidate")
else:
    print("Status: Average Candidate")