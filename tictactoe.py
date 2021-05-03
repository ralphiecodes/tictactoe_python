#Tic Tac Toe Game
#By Rafael Perez
#@ralphiecodes

def check_win(board,mark,player1,player2,my_board,re_board):
   
   global game_end
   #horizontal win
   if(board[7] == mark and board[8] == mark and  board[9] == mark):
       print('Game is over  ' + player1[0] + ' has won')
   
       board_display(my_board,re_board)
       game_end = True
       game_start()
   elif(board[4] == mark and board[5] == mark and board[6] == mark):
       print('Game is over  ' + player1[0] + ' has won')
       board_display(my_board,re_board)
       game_end = True
       game_start()
   elif(board[1] == mark and board[2] == mark and  board[3] == mark):
       print('Game is over  ' + player1[0] + ' has won')
       
       board_display(my_board,re_board)
       game_end = True
       game_start()
   #diagonal win
   elif(board[1] == mark and board[5] == mark and board[6] == mark):
       print('Game is over  ' + player1[0] + ' has won')
       
       board_display(my_board,re_board)
       game_end = True
       game_start()
   elif(board[3] == mark and board[5] == mark and board[7] == mark):
       print('Game is over  ' + player1[0] + ' has won')
       
       board_display(my_board,re_board)
       game_end = True
       game_start()
   #vertical win
   elif(board[1] == mark and board[4] == mark and board[7] == mark):
       print('Game is over  ' + player1[0] + ' has won')
       
       board_display(my_board,re_board)
       game_end = True
       game_start()
   elif(board[2] == mark and board[5] == mark and  board[8] == mark):
       print('Game is over  ' + player1[0] + ' has won')
       
       board_display(my_board,re_board)
       game_end = True
       game_start()
   elif(board[3] == mark and  board[6] == mark and  board[9] == mark):
       print('Game is over  ' + player1[0] + ' has won')
       
       board_display(my_board,re_board)
       game_end = True
       game_start()
   else:
       pass
          
def game_start():
    player1 = ['']
    player2 = ['']
    game_end = False
    response = ''
    test_board =['#','X','X','X','O','X','O','X','O','X']
    my_board =['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    re_board =['#','1','2','3','4','5','6','7','8','9']
    if game_end == True:
        response = input('Would you like to play again? Y or N')
        if response == 'Y':
            game_end = False
        else:
            game_end = True
    else:
        print('Welcome to Tic Tac Toe! by @ralphiecodes')
        player_choice(player1, player2)
        board_display(my_board,re_board)
        print(player1,player2)




        while game_end == False:
            if my_board[-1] == 'X' or  my_board[-1] == 'O':
               game_end = True

            else:
                position = int(input(f"Select your position: {player1[0]}"))
                my_board[position] = player1[0]
                check_win(my_board,player1[0],player1, player2,my_board,re_board)
                board_display(my_board,re_board)
                position = int(input(f"Select your position: {player2[0]}"))
                my_board[position] = player2[0]
                board_display(my_board,re_board)
                check_win(my_board,player2[0],player1,player2,my_board,re_board)
        

            



def board_display(board,board_two):
    print('Main Board' + '      ' + 'Reference Board')
    print(board[7] + '|' + board[8] + '|' + board[9] + '           ' + board_two[7] + '|' + board_two[8] + '|' + board_two[9])
    print(board[4] + '|' + board[5] + '|' + board[6] + '           ' + board_two[4] + '|' + board_two[5] + '|' + board_two[6])
    print(board[1] + '|' + board[2] + '|' + board[3] + '           ' + board_two[1] + '|' + board_two[2] + '|' + board_two[3])





def player_choice(player1,player2):

    while player1[0] != "X" and player1[0] != "O":
        player1[0] = input('Player 1 please choose either "X" or "O" ')
        if player1[0] == 'X':
            player2[0] = 'O'
        else:
            player2[0] = 'X'
    print(f'Player 1 is = {player1[0]} \nPlayer 2 is = {player2[0]}')
    

game_start()