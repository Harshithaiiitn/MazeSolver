import sys
def Fileparser(input_file):
    if inputs>=2:
        input_file=sys.argv[1]
        try:
            board = open(input_file).read()
            print('File readed successfully!!')
            board=[item.split() for item in board.split('\n')]
            display(board)
            moves(board)
        except:
            print('File not found')
def display(board):
    board_size=len(board)
    for row in range(0,board_size):
        for col in range(0,board_size):
            print("%-2s"%(board[row][col]),end='  ')
        print()
        
def moves(board):
    input_sequence=input('Enter input sequence : ')
    print(input_sequence)

if __name__=='__main__':

    inputs=len(sys.argv)
    Fileparser(inputs)