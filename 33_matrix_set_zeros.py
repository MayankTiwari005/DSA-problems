# leetcode 73

def brute(self, matrix, row, col):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(0,r):        # row changes
        if matrix[i][col] != 0:
            matrix[i],[col] = float("inf")
        
    for j in range(0,c):        # column changes
        if matrix[row][j] != 0: 
            matrix[i][col] = float("inf")

def setZeros(self, matrix) -> None:
    r = len(matrix)
    c = len(matrix[0])
    for i in range(0,r):
        for j in range(0,c):
            if matrix[i][j] == 0:
                self.brute(matrix,i,j)
    
    for i in range(0,r):
        for j in range(0,c):
            if matrix == float("inf"):
                matrix[i][j] = 0


def optimal(self, matrix):
    r = len(matrix)
    c = len(matrix[0])
    row_track = [0 for _ in range(r)]
    col_track = [0 for _ in range(c)]

    for i in range(0,r):
        for j in range(0,c):
            if matrix[i][j] == 0:
                row_track = -1
                col_track = -1
    
    for i in range(0,r):
        for j in range(0,c):
            if row_track[i] == -1 or col_track[j] == -1:
                matrix[i][j] = 0
        