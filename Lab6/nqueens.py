from copy import copy

def printSoln(solution):
    for row in solution:
        printable = ". "*row + "Q " + ". "*(n-row-1)
        print(printable)

def solve(n):
    indices = []
    solutions = placeQueens(n,indices)
    printSoln(solutions)

def placeQueens(n,indices):
    if len(indices) == n:
        return indices
    for i in range(n):
        if safeIndex(i,indices):
            newindices = copy(indices)
            newindices.append(i)
            soln = placeQueens(n,newindices)
            if len(soln) != 0:
                return soln
    return []

def safeIndex(i,indices):
    if i in indices: return False
    if len(indices) == 0: return True
    j = len(indices)
    for y,x in enumerate(indices):
        if abs(x-i) == abs(y-j): return False
    return True

if __name__ == "__main__":
    print("Please enter size of board: ")
    n = int(input())
    solve(n)