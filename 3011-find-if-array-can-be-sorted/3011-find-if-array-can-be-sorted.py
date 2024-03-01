class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        bitGroup = -1
        mp = defaultdict(list)
        bitCount = defaultdict(int)
        
        order = []
        for i in range(len(nums)):
            
            num = nums[i]
            count = 0
            while num:
                num -= num & -num
                count += 1
                
            
            if bitGroup != count:
                bitCount[count] += 1
                order.append((count,bitCount[count]))
            
            mp[(count, bitCount[count])].append(nums[i])
            
            bitGroup = count
    
        
        for key in mp:
            mp[key].sort()
            
            
        new = []
        
        for i in range(len(order)):
            new += mp[order[i]]
        
        compare = sorted(new)
        
        return compare == new
            
        