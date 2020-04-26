from copy import deepcopy

#Global Variables
QUEEN = 'Q'
BLOCK = '*'
FREE = 'F'
board_success_array = []

#Print Board
def print_board(board):
    board_size = len(board[0])

    for i in range(board_size) :
        print(board[i])


#This function return the empty board
def build_board (board_size):
    board =[]
    for i in range(board_size) :
        column = []
        for j in range(board_size):
            column.append(FREE)

        board.append(column)

    return board


#This function will mark all the positions that are not available
#input is currrent board status and  queen position (x,y)
def update_board (board,queen_row_ind,queen_col_ind):
    board_size = len(board[0])

    for i in range(board_size):
        # block row
        board[queen_row_ind][i] = BLOCK

        for j in range(board_size):
            # update column
            board[j][queen_col_ind] = BLOCK

            # block diagonal
            if ((queen_row_ind+queen_col_ind ) == (i+j) )or ((queen_row_ind-queen_col_ind ) == (i-j)) :
                board[i][j] = BLOCK

           # if (queen_row_ind+queen_row_ind )+2 == i+j or (queen_row_ind-queen_row_ind ) == i-j :
           #     board[i][j] = BLOCK


    #Add Queen Position
    board[queen_row_ind][queen_col_ind] = QUEEN

    return board

#This function check what position are available in the column
#input is current board and column index
def get_free_cells(board,column_ind):
    board_size = len(board[0])

    #list of available columns
    available_col_index = []

    for i in range(board_size):
        if board[i][column_ind] == FREE:
            available_col_index.append(i)

    return available_col_index







#This function will start at 0,0 and keep on
def get_board_positions (board,queen_col_ind) :
    board_size = len(board[0])
    # Get available free column locations in the
    free_cells = get_free_cells(board, queen_col_ind)

    if len(free_cells) == 0 :
        return None
    else:
        #iterate through each free cell and set queen and pass next
        for free in free_cells :
            board_copy = deepcopy(board)
            #set queen on board
            update_board(board_copy, free, queen_col_ind)
            #start next recusrsive call
            return_board = None
            if queen_col_ind < board_size -1 :
                #move to next column with current board position.
                return_board = get_board_positions(board_copy,queen_col_ind+1)
            else :
                #if all column iterations are succesful it means board is success.
                board_success_array.append(board_copy)


        return board_copy



def main():
     size = int(input("Please Enter board size either lenght or width:"))
     #-----------------------
     new_board = build_board(size)
     #call functon with board and start position as argument
     get_board_positions(new_board,0)

     i = 1
     for board_succ in board_success_array :
            print("Count :" , i)
            i+=1
            print_board(board_succ)


     print("Total combinationation for :",size , " are ", len(board_success_array))

main()
