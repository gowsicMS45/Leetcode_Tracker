# Last updated: 8/24/2026, 6:12:33 PM
class Solution(object):
    def generate(self, numRows):
        result =[]
        for i in range(numRows):
            row=[1] * (i+1)
            for j in range (1,i):
                row[j]=result[i-1][j-1] + result[i-1][j]
            result.append(row)
        return result 