class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        #is binary search possible?
        c = Counter(nums)
        mn = min(c.values())
        top = mn + 1
        res = 0
        #print(c)
        #print(top)
        
        
        for i in range(1, mn + 1):
            valid = True
            count = 0
            for val in c.values():
                
                a = val / (i + 1)
                b = val % (i + 1)
                if b == 0:
                    count += a
                elif i - b <= a:
                    count += math.floor(a) + 1
                else:
                    valid = False
                    break
                
            if valid:
                res = count
        
        return int(res)