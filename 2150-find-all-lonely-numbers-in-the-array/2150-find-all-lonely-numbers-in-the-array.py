class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        s = Counter(nums)
        res = []
        for key,val in s.items():
            
            if val == 1 and key -1 not in s and key + 1 not in s: 
                res.append(key)
        
        
        return res