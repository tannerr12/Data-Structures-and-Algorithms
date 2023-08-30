from sortedcontainers import SortedList

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        #2,1
        #1,1,1
        #1,8
        #1,7
        #1,6
        #1,5
        #1,4
        #1,3
        #1,2
        #1,1
        #find cost to split into target
        #def dfs(num, target):
        
        #2,2,3,3,4
        #3,3,4       
        
        mn = nums[-1]
        nxt = [0] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            mn = min(mn, nums[i])
            nxt[i] = mn
            
        #print(nxt)
        sl = SortedList()
        cost = 0        
        '''
        for i in range(len(nums)):
            if nums[i] % nxt[i] != 0:
                cost += 1
            dist = math.ceil(nums[i] / nxt[i]) - 1
            cost += dist
            sl.add(nxt[i])
        return cost 
        '''
        # 79,79,79,79,33 
        mn = nums[-1]
        for i in range(len(nums)-1,-1,-1):
            
            if mn < nums[i]:
                mod = nums[i] % mn
                if mod == 0:
                    cost += (nums[i] // mn) - 1
                else:
                    cost += math.ceil(nums[i] / mn) -1
                    avg = nums[i] // math.ceil(nums[i] / mn)
                    #dist = (mn - mod) // 2
                    mn = avg
                
            else:
                mn = nums[i]
            
        
        return cost