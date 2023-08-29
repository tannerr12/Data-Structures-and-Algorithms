class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        leftS = [0] * (n+1)
        rightS = [0] * (n+1)
        
        for i in range(n):
            
            val = customers[i]
            val2 = customers[n-i-1]
            
            if val == 'Y':
                leftS[i+1] = leftS[i] +1
            else:
                leftS[i+1] = leftS[i]
            
            if val2 == 'N':
                rightS[n-i-1] = rightS[n-i] + 1
            else:
                rightS[n-i-1] = rightS[n-i]
            
        
        total = []
        
        for i in range(n+1):
            total.append(leftS[i] + rightS[i])
            
        return total.index(max(total))
        