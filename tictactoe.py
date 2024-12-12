import random


def draw_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def input_player_letter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input('X or O? ').upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Human'


def make_move(board, letter, move):
    board[move] = letter


def is_winner(board, letter):
    return (
            (board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[7] == letter and board[4] == letter and board[1] == letter) or
            (board[8] == letter and board[5] == letter and board[2] == letter) or
            (board[9] == letter and board[6] == letter and board[3] == letter) or
            (board[7] == letter and board[5] == letter and board[3] == letter) or
            (board[1] == letter and board[5] == letter and board[9] == letter)
    )

def get_board_copy(board):
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy

def is_space_free(board, move):
    return board[move] == ' '

def get_player_move(board):
    move = " "
    while move not in '1 2 3 4 5 6 7 8 9'.split(" ") or not is_space_free(board, int(move)):
        move = input("Enter your move (1-9): ")
    return int(move)

def choose_random_move_from_list(board, moveList):
    possible_moves = []
    for i in moveList:
        if(is_space_free(board, i)):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        boardCopy = get_board_copy(board)
        if is_space_free(boardCopy, i):
            make_move(boardCopy, computerLetter, i)
            if is_winner(boardCopy, computerLetter):
                return i

    for i in range(1, 10):
        boardCopy = get_board_copy(board)
        if is_space_free(boardCopy, i):
            make_move(boardCopy, playerLetter, i)
            if is_winner(boardCopy, playerLetter):
                return i

    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move

    if is_space_free(board, 5):
        return 5

    return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False

    return True

print("Game TICTACTOE")

while True:
    board = [' ']*10
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print(turn+ ' goes first')
    game_is_playing = True

    while game_is_playing:
        if turn == 'Human':
            draw_board(board)
            move = get_player_move(board)
            make_move(board, player_letter, move)

            if is_winner(board, player_letter):
                draw_board(board)
                print('You win')
                game_is_playing = False
            else:
                if is_board_full(board):
                    draw_board(board)
                    print("DRAW")
                    break
                else:
                    turn = "Computer"
        else:
            move = get_computer_move(board, computer_letter)
            make_move(board, computer_letter, move)

            if is_winner(board, computer_letter):
                draw_board(board)
                print('Computer wins')
                game_is_playing = False

            else:
                if is_board_full(board):
                    draw_board(board)
                    print("DRAW")
                    break
                else:
                    turn = 'Human'


    if not input('Do you want to restart (yes or no)').lower().startswith('y'):
        break




