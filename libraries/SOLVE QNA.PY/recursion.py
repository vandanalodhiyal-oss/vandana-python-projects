#recursive function

def show (n):
    if(n==0):  #base case
        return
    print(n)
    show(n-1)

show(10)

#guess the number

def guess_game():
    number = 5   # computer ne number choose kiya
    
    guess = int(input("Guess the number (1-10): "))
    
    if guess == number:
        print("Correct!")
    else:
        print("Wrong! Try again")

guess_game()

#even odd 

def even_odd_game():
    num = int(input("Enter a number: "))
    
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

even_odd_game()


def city_game():
    city = input("Enter a city name: ")

    if city == "Delhi":
        print("Delhi is the capital of India")
    elif city == "Mumbai":
        print("Mumbai is the financial capital")
    elif city == "Haldwani":
        print("Haldwani is in Uttarakhand")
    else:
        print("City not in list")

city_game()







