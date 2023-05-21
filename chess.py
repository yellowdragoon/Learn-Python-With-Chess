# Define the chessboard as a list of lists
board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
         ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]

# Display the chessboard
def print_board(board):
    for row in board:
        print('+---' * 8 + '+')
        print('| ' + ' | '.join(row) + ' |')

    print('+---' * 8 + '+')

def letter_to_number(letter):
    return ord(letter) - ord('a')

def move(board, _from, _to):
    row_from = 8 - int(_from[1])
    row_to = 8 - int(_to[1])
    col_from = letter_to_number(_from[0])
    col_to = letter_to_number(_to[0])

    if(board[row_from][col_from] != ' '):
        piece = board[row_from][col_from]
        board[row_from][col_from] = ' '
        board[row_to][col_to] = piece



if __name__ == '__main__':
    print_board(board)
    move(board, 'e2', 'e4')
    print_board(board)


