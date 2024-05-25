class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        maxIndex = (n-1) // 2

        for i in range(maxIndex+1):
            for j in range(i, n-i-1):
                auxVal = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = auxVal
