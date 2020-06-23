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
    guard1_row,guard1_column=find_position('g1',board)
    guard2_row,guard2_column=find_position('g2',board)
    brnjolf_row,brnjolf_column=find_position('b',board)
    exit_row,exit_column=find_position('e',board)
    print('guard1 poisition :'+str(guard1_row)+","+str(guard1_column))
    print('guard2 poisition :'+str(guard2_row)+","+str(guard2_column))
    print('Brynjolf poisition :'+str(brnjolf_row)+","+str(brnjolf_column))
    print('Exit position :'+str(exit_row)+","+str(exit_column)) 
    
def find_position(person,board):
    for row in range(0,len(board)):
        for col in range(0,len(board)):
            if board[row][col]==person:
                position_row,position_column=row,col
    return position_row,position_column

if __name__=='__main__':

    inputs=len(sys.argv)
    Fileparser(inputs)