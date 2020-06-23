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
    count=0
    for direction in range(0,len(input_sequence)):
        count=count+1
        if input_sequence[direction] =='l':
            print("we need to move in left direction")
            moves_count,board,brnjolf_row,brnjolf_column,guard1_row,guard1_column,guard2_row,guard2_column,exit_row,exit_column= movingLeft(count,input_sequence,board,brnjolf_row,brnjolf_column,guard1_row,guard1_column,guard2_row,guard2_column,exit_row,exit_column)

        elif input_sequence[direction] == 'r':
            print("we need to move in right direction")
        elif input_sequence[direction] == 'u':
            print("we need to move in upward direction")
        elif input_sequence[direction] == 'd':
            print("we need to move in downward direction")

def movingLeft(count,input_sequence,board,brnjolf_row,brnjolf_column,guard1_row,guard1_column,guard2_row,guard2_column,exit_row,exit_column):
    print("we need to invoke brynjolf move,guards moves in left direction")
    moves_count=0
    b_win,b_lose,flag,board,brnjolf_row,brnjolf_column=moveLeft('b',brnjolf_row,brnjolf_column,board,exit_row,exit_column)
    moves_count=moves_count+flag
    win,g1_lose,flag,board,guard1_row,guard1_column=moveLeft('g1',guard1_row,guard1_column,board,exit_row,exit_column)
    moves_count=moves_count+flag
    win,g2_lose,flag,board,guard2_row,guard2_column=moveLeft('g2',guard2_row,guard2_column,board,exit_row,exit_column)
    moves_count=moves_count+flag
    return moves_count,board,brnjolf_row,brnjolf_column,guard1_row,guard1_column,guard2_row,guard2_column,exit_row,exit_column
            
def moveLeft(person,current_row,current_column,board,exit_row,exit_column):
    column=current_column
    current_column=current_column-1
    win='false'
    lose='false'
    flag=0
    while current_column>=0:
        if board[current_row][current_column]=='F':
            board[current_row][current_column]=person
            board[current_row][current_column+1]='F'
            column=current_column
            current_column=current_column-1
            flag=1
        elif (board[current_row][current_column]=='e' and (person=='g1' or person=='g2')) or board[current_row][current_column]=='X':
            break
        elif (board[current_row][current_column]=='g1' or board[current_row][current_column]=='g2') and person=='b':
            board[current_row][current_column]=person
            board[current_row][current_column+1]='F'
            lose='true'
            break
        elif (person=='g1' or person=='g2') and board[current_row][current_column]=='b':
            board[current_row][current_column]=person
            board[current_row][current_column+1]='F'
            lose='true'
            break

        elif board[current_row][current_column]=='e' and person=='b':
            #board[current_row][current_column]=person
            board[current_row][current_column+1]='F'
            win='true'
            break  
    return win,lose,flag,board,current_row,column


def find_position(person,board):
    for row in range(0,len(board)):
        for col in range(0,len(board)):
            if board[row][col]==person:
                position_row,position_column=row,col
    return position_row,position_column

if __name__=='__main__':

    inputs=len(sys.argv)
    Fileparser(inputs)