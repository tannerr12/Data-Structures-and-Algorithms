class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        
        #Catalan numbers
        #https://mathshistory.st-andrews.ac.uk/Extras/Catalan/#:~:text=The%20Catalan%20numbers%3A%201%2C%202,number%20of%20problems%20in%20combinatorics.
        
        #this is a form of combinatorics that can be used to compute
        '''
        Polygons: the number of ways a polygon with 
        �
        +
        2
        n+2 sides can be cut into 
        �
        n triangles.
        Parentheses: the number of ways in which parentheses can be placed in a sequence of numbers to be multiplied, two at a time.
        Trees: the number of rooted, trivalent trees with 
        �
        +
        1
        n+1 nodes.
        Paths: the number of paths of length 
        2
        �
        2n through an 
        �
        ×
        �
        n×n grid that do not rise above the main diagonal,
        Stairs: the number of ways to decompose a staircase-shaped figure with 
        �
        n steps into 
        �
        n rectangles.
        '''
        MOD = 10**9 + 7
        dp = [0] * numPeople  
        dp[0] = 1
        
        for i in range(1,numPeople//2):
            dp[i] = dp[i-1] * 2 * (2*i+1)//(i+2) 
        

        
        return dp[(numPeople//2) -1] % MOD