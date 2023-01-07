class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        
        l,r = 0, minutes -1
        rsum = 0
        for i in range(r+1):
            if grumpy[i]:
                rsum+= customers[i]
        res = 0
        rall = 0 
        while r <= len(customers):
        
            res = max(rsum, res)
            
            r+=1
            if r == len(customers):
                break
            if grumpy[r]:
                rsum += customers[r]
            
            if grumpy[l]:
                rsum -= customers[l]
            l+=1
        
        
        for i in range(len(customers)):
            if grumpy[i] == 0:
                rall += customers[i]
                
        return rall + res
            