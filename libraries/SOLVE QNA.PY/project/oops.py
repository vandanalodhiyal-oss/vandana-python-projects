#qus1

class Demo:
    
    def __init__ (self):
     print("Constructor called")
    
d1 = Demo()
d2 = Demo()


#qus2

class bike:
   color = "black"
   brand = "royal enfield"

bike1 = bike()
print(bike1.color)
print(bike1.brand)

#qus3

class student:
   
  def __init__ (self , name):
      self.name = name

  def show(self):
         print(self.name)

s1 = student("vandana")
s2 = student("vannu")

s1.show()
s2.show()


#qus4  

class test:

    def __init__(self):
        print("A")

    def show(self):
        print("B")

t1 = test()
t2 = test()

t1.show()
t2.show()


#qus5

class Demo:

    def __init__(self):
        print("constructor")

    def show(self):
        print("Hello")

d1 = Demo()
d2 = Demo()

d1.show()
d2.show()    