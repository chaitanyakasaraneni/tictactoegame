import random
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[1]+' | ' +board[2]+' | '+board[3])
    print('--|---|--')
    print(board[4]+' | ' +board[5]+' | '+board[6])
    print('--|---|--')
    print(board[7]+' | ' +board[8]+' | '+board[9])

def player_input():
    choice=''
    while choice!='X' and choice!='O':
        choice=input('Player1, Enter your choice as X or O:').upper()
    if choice=='X':
        return ('X','O')
    elif choice=='O':
        return ('O','X')

def place_marker(board, marker, position):
    board[position]=marker

def win_check(board, mark):
    for i in range (1,4):
        x= board[i]== board[i+1] == board[i+2]==mark
    for i in range (1,4):
        y= board[i]== board[i+3] == board[i+3]==mark
    z = (board[1]==board[5]==board[9]==mark)
    a = (board[3]==board[5]==board[7]==mark)
    return x or y or z or a

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player2's turn.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
