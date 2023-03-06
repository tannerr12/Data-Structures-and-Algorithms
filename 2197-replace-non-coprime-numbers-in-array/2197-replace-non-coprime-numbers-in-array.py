class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        
        def lcm(a,b,gc):
            return a*b//(gc)
        res = []
        
        i = 0
        
        
        #check gcd between index and top of stack and pop both and merge new value
        #check 2 top values in stack and pop/merge them if gcd
        #return the stack
        while i < len(nums):
            
            if i == 0:
                res.append(nums[i])
                
            else:
                
                g = gcd(nums[i],res[-1])
                while i < len(nums) and res and g > 1:
                    v = res.pop()
                    res.append(lcm(nums[i],v,g))
                    i+=1
                    if i < len(nums):
                        g = gcd(nums[i],res[-1])
                
                g = 0
                if len(res) > 1:
                    g = gcd(res[-1], res[-2])
                while len(res) >= 2 and g > 1: 
                    v1,v2 = res.pop(),res.pop()
                    res.append(lcm(v1,v2,g))
                    g= 0
                    if len(res) > 1:
                        g = gcd(res[-1], res[-2])

                if g <= 1 and i < len(nums):
                    res.append(nums[i])
            
            i+=1

            
        return res