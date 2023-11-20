class trie:
    
    def __init__(self, val):
        self.adj = {}
        self.val = val
        self.mn = float('inf')
        self.mx = 0

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums = list(set(nums))
        res = 0
        maxNum = max(nums)
        mxBit = 0
        for i in range(20):
            if maxNum & (1 << i) > 0:
                mxBit = i
        #print(1 ^ 1)
        
        #xor TRIE
        #could check based on maximum bit postion against all numbers with that postion but n 2
        #the numbers would need to be sorted so that we can check the min / max ranges  <- ->
        
        t = trie(0)
        
        for i in range(len(nums)):
            tri = t
            t.mn = min(nums[i], t.mn)
            t.mx = max(nums[i], t.mx)
            for j in range(mxBit,-1,-1):
                val = 1 if nums[i] & (1 << j) > 0 else 0
                if val in tri.adj:
                    tri = tri.adj[val]
                else:
                    tri.adj[val] = trie(val)
                    tri = tri.adj[val]
                tri.mx = max(tri.mx, nums[i])
                tri.mn = min(tri.mn, nums[i])
                    
        #add some math to our pathfinding to make sure we pick a valid path 2 ** layer is our max value to add
        #what if that is not within our target range? we may need to purposly take 1 or 0
        
        #001000001000
        #100111000100
        
        for i in range(len(nums)):
            tri = t
            number = 0 
            upper = nums[i] * 2
            #lower = nums[i] // 2
            #print('****')
            #print(nums[i])
            valid = True
            for j in range(mxBit,-1,-1):
                val = 1 if nums[i] & (1 << j) > 0 else 0
                target = 0 if val else 1
                
                #print(tri.mx)
                #print(tri.mn)
                if (target in tri.adj) and tri.adj[target].mn <= upper and tri.adj[target].mx * 2 >= nums[i]:
                    number |= (target << j)
                    tri = tri.adj[target]
                elif val in tri.adj and tri.adj[val].mn <= upper and tri.adj[val].mx * 2 >= nums[i]:
                    number |= (val << j)
                    tri = tri.adj[val]
                else:
                    valid = False
                    break
                
                #print(number)
            
            #|x - y| <= min(x, y)
            #print('****')
            #print(nums[i])
            #print(number)
            #print(nums[i] ^ number)
            #print('####')
            if abs(nums[i] - number) <= min(nums[i], number) and valid:
                res = max(res, nums[i] ^ number)
        
        return res

            