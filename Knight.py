'''Given an 8*8 empty chessboard in which a knight is placed at a position (X, Y). Your task is to find the number of positions in the chessboard knight can jump into in a single move .
Note:- Rows and Columns are numbered through 1 to N.
Input
User Task:
Since this will be a functional problem, you don't have to take input. You just have to complete the function Knight() that take integers X and Y as arguments.

Constraints:-
1 <= X <= 8
1 <= Y <= 8
Output
Return the number of positions Knight can jump into in a single move.'''

# Solution
def Knight(x,y):
    if x==1 or x==8:
        if y==1 or y==8:
            return 2
        elif y==2 or y==7:
            return 3
        else:
            return 4
    elif x==2 or x==7:
        if y==1 or y==8:
            return 3
        elif y==2 or y==7:
            return 4
        else:
            return 6
    else:
        if y==1 or y==8:
            return 4
        elif y==2 or y==7:
            return 6
        else:
            return 8
