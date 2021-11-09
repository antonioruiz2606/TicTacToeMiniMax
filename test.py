from tictactoe import minimax

X = "X"
O = "O"
EMPTY = None

board = [[X, O, X],
        [EMPTY, O, EMPTY],
        [X, EMPTY, EMPTY]]

def main(): 
    print(minimax(board))
    return None

if __name__ == '__main__':
    main()