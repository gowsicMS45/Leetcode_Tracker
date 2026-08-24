# Last updated: 8/24/2026, 12:21:51 PM
class Solution(object):
    def convert(self, s, numRows):
        if numRows== 1 :
            return s
        rows = [''] * numRows
        row , step =0,1
        for ch in s:
            rows[row] += ch 
            if  row == 0:
                step = 1
            elif row == numRows -1:
                step =-1
            row += step
        return "".join(rows)



      
        