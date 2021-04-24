board = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]


#This program takes an unsolved sudoko game in the form of a double dimension array in the variable  'board' and then using the backtracking algoritm
#and attempts to solve it using the backtracking algoritm

def print_grid(sudo):
    for i in range(0, 9):
        print(sudo[i])
        print()


def value_safe(sudo, row, col, num):
    flag = True
    # row check
    for i in range(0, 9):
        if sudo[row][i] == num:
            flag = False
    # coloumn check
    for i in range(0, 9):
        if sudo[i][col] == num:
            flag = False
    # matrix check
    mat_row = row - row % 3
    mat_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudo[i + mat_row][j + mat_col] == num:
                flag = False
    return flag


def solve(sudo, row, col):


    if row ==8 and col ==9:
        self.board = sudo
        return True

    if col == 9:
        row = row + 1
        col = 0

    if sudo[row][col]!=0:
        return solve(sudo, row, col + 1)

    for num in range(1,10):
          if value_safe(sudo,row,col,num):
             sudo[row][col]=num
             print("Step:")
             print_grid(sudo)

             if solve(sudo,row,col):
                 return True

          sudo[row][col]=0
    print("Backtracking")
    return False



if solve(sudo=board, row=0, col=0):
    print("Solution:")
    print_grid(board)
else:
    print("Unsolvable suduko")