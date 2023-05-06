class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        if runningCost > boardingCost * 4:
            return -1
        #dont need to let customers exit this is assumed
        res = [0,0]
        line = 0
        profit = 0
        for i in range(len(customers)):
            
            #load customers 
            if customers[i] >= 4:
                #load up the max
                profit += (4 * boardingCost) - (runningCost)
                line += max(customers[i] - 4, 0)
            else:
                if line >= 4 - customers[i]:
                    line -= 4 - customers[i]
                    profit += (4 * boardingCost) - (runningCost)
                else:
                    profit += ((line + customers[i]) * boardingCost) - (runningCost)
                    line = 0
            
            
            if profit > res[1]:
                res = [i+1, profit]
        
        
        i = len(customers) +1
        while line:
            if line >= 4:
                profit += (4 * boardingCost) - (runningCost)
                line -= 4
            else:
                profit += (line * boardingCost) - (runningCost)
                line = 0
            if profit > res[1]:
                res = [i, profit]
            i += 1
            
        #print(res)
        return res[0] if res[1] > 0 else -1
            
            
            
            
        