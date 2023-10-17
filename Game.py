import random

# List containing 4 fruits to be randomized
Fruit_List = ['ORANGE', 'BANANA', 'DURIAN', 'PAPAYA']

# List containing randomized 4 fruits to be guessed
Random_Fruits = []

# Assigning intial correct fruit at correct place count equal to 0
Correct_Fruit_Correct_Place = 0

# Assigning intial correct fruit at correct wrong count equal to 0
Correct_Fruit_Wrong_Place = 0

# Assigning intial wrong fruit equal to 0
Wrong_Fruit = 0

# Confirmation
Confirm = None

# List containing the user input's fruits
User_List = []

# Assigning intial number of total tries count equal to 0
Total_Tries = 0


# Introduction to the Master Mind game
def Main_Menu():
    print('**************************WELCOME TO A MASTERMIND COMPUTER GAME**************************')
    print()
    print('************************************RULES OF THE GAME************************************')
    print('1) Four fruits will be generated randomly from the list below:')
    print('[orange,banana,durian,papaya]')
    print('2) From the above list of fruits, you are required to guess the randomly generated lists of fruits')
    print('3) The game will give a feedback of how many fruits are guessed correctly with the correct position')
    print('4) The game will also give a feedback of how many fruits are guessed correctly but in the wrong place')
    print()
    print('**********************GOODLUCK,JUST PLAY,HAVE FUN AND ENJOY THE GAME*********************')
    print()


Main_Menu()


# Commencing the game if player is ready
def gamestart():
    global Random_Fruits
    while Confirm not in ('YES', 'NO'):
        Confirmation = input('Are you ready to begin? Enter YES or NO: ').upper()

        if Confirmation == 'YES':
            print('***********************************The Game Begins***********************************')
            print('List of fruits to be chosen: [ORANGE, BANANA, DURIAN, PAPAYA]')
            Random_Fruits = random.choices(Fruit_List, k=4)
            #print('Random fruits = ', Random_Fruits)
            break

        elif Confirmation == 'NO':
            print('********************Begin When You Are Ready to Face The Challenge********************')

        else:
            print('*******************************PLEASE ENTER YES OR NO********************************')


gamestart()


# User will enter their choices of fruits and error validation ensures user's choice of fruits are as the listed fruits
def Checking_User_Input():
    Counter = 1
    while Counter <= 4:
        User_Input = str(input('Enter your choice of fruits in sequence: ').upper())
        if User_Input in Fruit_List:
            User_List.append(User_Input)
            Counter += 1
        else:
            print('Please enter the correct fruit as listed')

    print('Your choices of fruits = ', User_List)
    return User_List


Checking_User_Input()


# Checking how many fruits the user has entered correctly in the correct place, wrong place and how many wrong fruit
def Check_correct():
    global Correct_Fruit_Correct_Place, Correct_Fruit_Wrong_Place, Wrong_Fruit, Total_Tries
    while Correct_Fruit_Correct_Place != 4:

        for i in range(len(User_List)):
            if User_List[i] == Random_Fruits[i]:
                Correct_Fruit_Correct_Place += 1
            elif User_List[i] in Random_Fruits:
                Correct_Fruit_Wrong_Place += 1
            else:
                Wrong_Fruit += 1

        Total_Tries += 1

        if Correct_Fruit_Correct_Place != 4:
            print('Correct fruits in the correct place: ', Correct_Fruit_Correct_Place)
            print('Correct fruits in the wrong place: ', Correct_Fruit_Wrong_Place)
            print('Wrong fruits: ', Wrong_Fruit)
            print()
            print('Oh no, your choice did not match.Please try again.')

            User_List.clear()
            Correct_Fruit_Correct_Place = 0
            Correct_Fruit_Wrong_Place = 0
            Checking_User_Input()
        else:
            print('Congratulations, you have guessed the correct fruits in the correct place!')
            print('Total number of tries: ', Total_Tries)

Check_correct()


# Asking the user whether he or she wants to play again

def Play_Again():
    global Confirm, Correct_Fruit_Correct_Place, Correct_Fruit_Wrong_Place, Wrong_Fruit, Total_Tries
    print()
    print('**********Do you want to play again*********')
    Restart = input('Please enter Yes or No: ').upper()

    if Restart == 'YES':
        Confirm = None
        User_List.clear()
        Correct_Fruit_Correct_Place = 0
        Correct_Fruit_Wrong_Place = 0
        Wrong_Fruit = 0
        Total_Tries = 0
        Main_Menu()
        gamestart()
        Checking_User_Input()
        Check_correct()
        Play_Again()
    elif Restart == 'NO':
        print('Thanks for playing, see you again!')
        exit()
    else:
        print('********************************PLEASE ENTER YES OR NO********************************')
        Play_Again()


Play_Again()
