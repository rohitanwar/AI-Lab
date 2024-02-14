from copy import deepcopy

def printSoln(solution):
    for row in solution:
        for el in row:
            print(el,end=" ")
        print("")

def solve(n):
    board = [[0]*n for i in range(n)]
    solutions = placeQueens(0,board)
    for i, solution in enumerate(solutions):
        print(f"Solution {i}: ")
        printSoln(solution)

def placeQueens(n,board):
    indices = []
    for row in board:
        if 1 in row:
            indices.append(row.index(1))
    if len(indices) == len(board):
        return [board]
    solutions = []
    for i in range(len(board)):
        if safeIndex(i,indices):
            newboard = deepcopy(board)
            newboard[len(indices)][i] = 1
            solutions += placeQueens(n+1,newboard)
    return solutions

def safeIndex(i,indices):
    if i in indices: return False
    if len(indices) == 0: return True
    j = len(indices)
    for y,x in enumerate(indices):
        if abs(x-i) == abs(y-j): return False
    return True

solve(8)
