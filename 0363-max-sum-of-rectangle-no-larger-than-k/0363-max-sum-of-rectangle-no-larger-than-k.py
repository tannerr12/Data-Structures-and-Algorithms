class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        
        # Getting the dimensions of the matrix
        m, n = len(matrix), len(matrix[0])
        
        # Initializing the maximum sum
        max_sum = -float('inf')
        
        # Iterating over all the columns
        for left in range(n):
            
            # Initializing the temporary sum list
            temp = [0] * m
            
            # Iterating over all the columns to the right of left
            for right in range(left, n):
                
                # Adding the values of the current column to temp
                for i in range(m):
                    temp[i] += matrix[i][right]
                
                # Kadane's algorithm to find the maximum sum of a subarray with sum less than or equal to k
                cum_sum = 0
                cum_sum_set = sorted([0])
                
                for t in temp:
                    cum_sum += t
                    it = bisect_left(cum_sum_set, cum_sum - k)
                    if it != len(cum_sum_set):
                        max_sum = max(max_sum, cum_sum - cum_sum_set[it])
                    bisect.insort(cum_sum_set, cum_sum)
        
        # Returning the maximum sum found
        return max_sum