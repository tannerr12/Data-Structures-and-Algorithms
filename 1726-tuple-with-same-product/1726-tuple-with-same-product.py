class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                val= nums[i] * nums[j]
                mp[val] += 1
                
 
        
        """
        Gauss occurances - 1 
        than * 8
        """
        res = 0
        for key,val in mp.items():
            val -=1
            res += (val * (val + 1)) // 2

        return 8 * res