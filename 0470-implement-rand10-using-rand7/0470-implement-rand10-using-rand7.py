# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
import numpy as np
class Solution:
    def rand10(self):
        """
        :rtype: int
        """

        row,col,idx = 41,41,41
        
        while idx > 40:
            
            row = rand7()
            col = rand7()
            
            idx = col + (row -1) * 7
            
        
        return 1 + (idx - 1) % 10