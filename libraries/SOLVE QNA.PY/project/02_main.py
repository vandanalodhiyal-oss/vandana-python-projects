#student manegement system

class Student:       #ek clss bnai jiska name student rakha

    def __init__(self,name,roll,marks):
        self.name = name            #object ka name stor ho rha 
        self.roll = roll
        self.marks = marks

    def display(self):                #method jo student ki detail print krega krega
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("Marks:",self.marks)

s1 = Student("vandana",50,55)         #student class ka object s1 bnaya or value di
s2 = Student("vannu",88,90)

s1.display()     # s1 object ki detail print karega
s2.display()     