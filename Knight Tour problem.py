# Python3 program to solve Knight Tour problem using Backtracking

 

# Chessboard Size

n = 8

 

 

def isSafe(x, y, board):

    '''

        A utility function to check if i,j are valid indexes

        for N*N chessboard

    '''

    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):

        return True

    return False

 

 

def printSolution(n, board):

    '''

        A utility function to print Chessboard matrix

    '''

    for i in range(n):

        for j in range(n):

            print(board[i][j], end=' ')

        print()

 

 

def solveKT(n):

    '''

        This function solves the Knight Tour problem using

        Backtracking. This function mainly uses solveKTUtil()

        to solve the problem. It returns false if no complete

        tour is possible, otherwise return true and prints the

        tour.

        Please note that there may be more than one solutions,

        this function prints one of the feasible solutions.

    '''

 

    # Initialization of Board matrix

    board = [[-1 for i in range

