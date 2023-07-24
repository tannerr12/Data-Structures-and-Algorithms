class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        #if any number mod k ==0 than it pairs with everything
        
        # 1 * 2, 1 * 3, 1 * 4, 1 * 5= 2,3,4,5
        # 2 * 3, 2 * 4, 2 * 5 = 6,8,10
        # 3 * 4, 3 * 5 = 12, 15
        # 4 * 5 = 20

        c = Counter()
        res = 0
        
        for i in range(len(nums)):
            x = gcd(nums[i], k)
            want = k // x
            
            for key in c:
                
                if key % want == 0:
                    res += c[key]
            
            c[x] += 1
        
        return res
        