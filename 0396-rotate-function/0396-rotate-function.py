class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        #0s dont matter
        
        """
        #brute force how can we compress this into linear
        res = 0
        for i in range(len(nums)):
            j = i + 1
            j %= len(nums)
            count = 1
            val = 0
            while j != i:
                
                val += nums[j] * count
                count +=1
                j+=1
                j %= len(nums) 
            
            res = max(res,val)
        
        return res
        """
        
        #we take the current prefix sum with mult as a start and assign that to p
        #we also take a total of all the values in the array and assign that to total
        #since each shift will subtract each number 1 time ex: 5 * 2 becomes 5 * 1 which is just subtracting its value in nums once
        #all we have to do to check the next value is take our current prefix sum - total which is our total without adding the new value
        #than + our new value * the length of the array since it will be at the end of the array
        
        #example 1: our starting prefix is 25 and our total is 15 we want to shift our starting position to nums[1] = 3 we do 25-15 = 10 than 10 + (4 * 4) = 26
        #Note: we had to wrap around our right pointer to the first position
        total = nums[0]
        p = 0
        for i in range(1,len(nums)):
            p = (nums[i] * i) + p
            total += nums[i]
        r = len(nums) -1
        res = float('-inf')
        for l in range(len(nums)):
            res = max(res, p)
            r +=1
            r %= len(nums)
            p = (p - total) + nums[r] * len(nums)
            
        
        return res
            