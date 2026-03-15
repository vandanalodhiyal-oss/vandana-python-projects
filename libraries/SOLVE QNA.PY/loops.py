# quetion 1  -------print number form 1to 100

i = 1
while i<= 100:
    print(i)
    i +=1

print()

#question 2------print the multiplication table of a number n.


i = 1
while i <=10:
    print(3 *i)
    i+=1




print()

#qus3-------print the elements of the following list using a loop:  [1,4,9,16,25,36,49,64,81,100]

num = (1,4,9,16,25,36,49,64,81,100)

idx = 0
while idx < len(num):
    print (num[idx]) #num[0] , num[1] , num[2]......
    idx +=1

print()

# qus4-------serch for number x in this tuple using loops:[1,4,9,16,25,36,49,64,81,100]

num = (1,4,9,16,25,36,49,64,81,100)

x=49

i=0
while i< len(num):
    if(num[i]==x):
        print("found" , i)
    i +=1


    print()

#qus 5----1 se 20 tak even no ka count

count = 0

for i in range(1, 11):
    if i % 2 == 0:
        count += 1

print("Total even no:", count)


print()

#qus6-------user se no lena or check karna prime hai ya nhi

num = int(input("enter a number:"))
count = 0

for i in range(1 , num + 1):
    if num % i == 0:
        count +=1

        if count ==2:
            print("prime number")
        else:
            print("not prime number")


print()

#qus7-------5 * 5 # pattern

for i in range(5):
    print ("#" *5)





    print()

#qus8----even odd sum alg  alg

even_sum = 0
odd_sum = 0


for i in range(1, 21):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Even numbers ka sum =", even_sum)
print("Odd numbers ka sum =", odd_sum)

print()

#qus9-----1 se 100 tk no main 3 or 5 se divisible ho vo no print

for i in range(1,101):
    if i % 3 ==0 and i % 5 ==0:
        print(i)
  
print()

#qus10-----user se no lena check krna prime hai ya nhi

num = int(input("Enter a number: "))

if num > 1:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")

print()

#fruit name print 3

fruit = ["apple" , "banana" , "mango"]

for i in fruit:
    print(i)

print()



