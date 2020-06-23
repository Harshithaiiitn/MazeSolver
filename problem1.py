import sys
def Fileparser(input_file):
    if inputs>=2:
        input_file=sys.argv[1]
        try:
            board = open(input_file).read()
            print('File readed successfully!!')
        except:
            print('File not found')
    

if __name__=='__main__':

    inputs=len(sys.argv)
    Fileparser(inputs)