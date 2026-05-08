import random

def Number_Game():
    userGuessedNum = int(input("Enter the number you are guessing from 0 to 3 :"))
    options = [0,1,2,3]
    computerChoice = random.choice(options)
    if (userGuessedNum == computerChoice) :
        print('congrats , you guessed the correct number')
    else :
        print(f'''Wrong , Your choice is {userGuessedNum} and computer choice is {computerChoice}.
               please try again''')
   
    return computerChoice

Number_Game()