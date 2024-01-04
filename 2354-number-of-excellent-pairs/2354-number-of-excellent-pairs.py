class trie:
    
    def __init__(self,val):
        
        self.val = 0
        self.adj = {}
        self.eon = False
        self.count = 0


class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        #add bits that are different + bits that are the same + different
        #at any given point in the tree for a number if we have enough points we can add the count here + below and stop that branch
        
        #bits = math.ceil(log(max(nums),2))
        s = set(nums)
        
        arr = []
        
        for val in s:
            bit = 0
            for i in range(math.ceil(log(val, 2)) + 1):
                if val & (1 << i) > 0:
                    bit += 1 
            
            arr.append(bit)
        
        arr.sort()
        
        res = 0
        
        for i in range(len(arr)):
            
            res += len(arr) - bisect_left(arr, k - arr[i])
        
        return res