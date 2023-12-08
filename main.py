import random
from IPython.display import clear_output


def board_display(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])



def user_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Choose X or O: ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position]=marker

def win_check(board, mark):
    return((mark == board[7] == board[8] == board[9]) or
            (mark == board[4] == board[5] == board[6]) or
            (mark == board[1] == board[2] == board[3]) or
            (mark == board[7] == board[4] == board[1]) or
            (mark == board[8] == board[5] == board[2]) or
            (mark == board[9] == board[6] == board[3]) or
            (mark == board[7] == board[5] == board[3]) or
            (mark == board[9] == board[5] == board[1]))





def choose_first():
    flip = random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board,position):
    return board[position] == ' '


def board_full(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    #board is full if it is true
    return True


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9,10] or not space_check(board, position):
        position = int(input("Choose a position: "))

    return position


def replay():
    replay_choice = input("Do you wanna play again: Y-N? ")
    if replay_choice == 'Y':
        return True


row = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

game_on = True
while True:

    the_board = [' ']*10
    player_1_marker, player_2_marker = user_input()

    turn = choose_first()
    print(turn + " will go first")

    play_game = input('Ready to play? Y o N: ')

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    #Gameplay is on

    while game_on:
        if turn == 'Player 1':
            #Show the board
            board_display(the_board)
            #Choose a position
            position = player_choice(the_board)
            #Place the marker on the position
            place_marker(the_board,player_1_marker, position)
            #check if it is a win?
            if win_check(the_board, player_1_marker):
                board_display(the_board)
                print('Player 1 is winner')
                game_on = False
            else:
                if board_full(the_board):
                    board_display(the_board)
                    print('It is a tie')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            # Show the board
            board_display(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player_2_marker, position)
            # check if it is a win?
            if win_check(the_board, player_2_marker):
                board_display(the_board)
                print('Player 2 is winner')
                game_on = False
            else:
                if board_full(the_board):
                    board_display(the_board)
                    print('It is a tie')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break

