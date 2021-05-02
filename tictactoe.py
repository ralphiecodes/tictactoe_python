#Tic Tac Toe Game
import time

#Global Variables
row1 = ['', '', '']
row2 = ['', '', '']
row3 = ['', '', '']

current_letter = ''
current_index = 0

# if player_one_turn == True:
#            player_one()
#        else:
#           player_two()
#


#Game Display
def display():
    print('Current Board')
    print(row1)
    print(row2)
    print(row3)

#Game start
def game():
    
    print('Hey! Welcome to Tic Tac Toe')
    time.sleep(1)
    display()
    
    x = input('Please enter X or O?')
    if x != 'end':
        phase_one(x)
        game()
    else:
        print('Game ended')
    
    

def phase_one(x):
    global current_letter
    if x == 'X' or x == 'x':
        current_letter = 'X'
        phase_two()
    elif  x == 'O' or x != 'o':
        current_letter = 'O'
        phase_two()
    else:
        print('Please enter valid input?')
        phase_one()

def phase_two():
    where = input("Where would you like to place it? ex: row1, row2, row3  ")
    global row1
    global row2
    global row3
    if where == 'row1':
        index = int(input('Tell me which index you would like to place it at? 0 for left, 1 for middle and 2 for right  '))
        if index == 0:
            row1[0] = current_letter
            display()
        elif index == 1:
            row1[1] = current_letter
            display()
        elif index == 2:
            row1[2] = current_letter
            display()
        else:
            pass
    elif where == 'row2':
        index = int(input('Tell me which index you would like to place it at? 0 for left, 1 for middle and 2 for right  '))
        if index == 0:
            row2[0] = current_letter
            display()
        elif index == 1:
            row2[1] = current_letter
            display()      
        elif index == 2:
            row2[2] = current_letter
            display()
        else:
            pass  
    elif where == 'row3':
        index = int(input('Tell me which index you would like to place it at? 0 for left, 1 for middle and 2 for right  '))
        if index == 0:
            row3[0] = current_letter
            display()
        elif index == 1:
            row3[1] = current_letter
            display()
        elif index == 2:
            row3[2] = current_letter
            display()
        else:
            pass
        
    else:
        print("Please enter valid row? ex: row1, row2, row3  ")
        phase_two()

    


def win():
    row = ''
    letter = ''
    if letter in row and 



# Validates user input
def user_choice(choice):
    if type(choice) == int:
        if choice not in [0,1,2]:
            print('You are out of range')
            time.sleep(1)
        else:
            pass
    elif type(choice) == str and len(choice) == 1:  
        pass
    else:
        print('Please enter a valid number? 0,1,2  ')

game()