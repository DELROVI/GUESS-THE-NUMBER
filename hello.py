import random

def guess_the_number():
    secret_number=random.randint(1,10)
     
     #Initialize variables
    attempts=0
    guesssed_Number =None

    print("Welcome to Guess The Number Game!")
    print("Try to guess the number 1 and 10")

    while guesssed_Number!=secret_number:
        try:
            guesssed_Number=int(input("Enter your guess : "))
            attempts+=1

            if guesssed_Number==secret_number:
                print(f"CONGRATULATIONS YOU GUESSED THE CORRECT NUMBER")
            elif(guesssed_Number<secret_number):
                print(f"TOO LOW TRY AGAIN")
            elif(guesssed_Number>secret_number):
                print(f"TOO HIGH TRY AGAIN")
        except ValueError:
            print("Invalid input. Please enter a valid number")
            
if __name__=="__main__":
    guess_the_number()