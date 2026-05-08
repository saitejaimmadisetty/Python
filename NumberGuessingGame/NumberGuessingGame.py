import random

def Number_Game():
    attempts = 0
    print('Guess a number between 0 to 9')
    computerChoice = random.randint(0,9)

    while True:
        try:
            userGuessedNum = int(input("Enter the number:"))
            attempts+=1
            if (userGuessedNum == computerChoice) :
                print(f'congrats , you guessed the correct number in {attempts} attempts')
                break 
            elif userGuessedNum<computerChoice :
                print("enter higher number")
            else :
                print('enter Lower number')

        except ValueError:
            print('Enter numeric values only')
   

Number_Game()