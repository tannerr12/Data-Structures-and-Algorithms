class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        #anything with a self loop should be ignored and any path that connects to it should be ignored
        #if a cycle goes forward anything that goes backwards should be ignored
        #same for negative these need to be seperated
        #a loop must have atleast 1 indegree
        
        parent = [i for i in range(len(nums))]
        rank = [0] * len(nums)
        
        
        def find(val):
            if val == parent[val]:
                return val
            
            parent[val] = find(parent[val])
            return parent[val]
        
        
        def union(x,y):
            
            v1,v2 = find(x), find(y)
            
            if v1 != v2:
                if rank[v1] > rank[v2]:
                    parent[v2] = v1
                elif rank[v2] > rank[v1]:
                    parent[v1] = v2
                else:
                    parent[v2] = v1
                    rank[v1] +=1
                    
                return False
            return True
        
        
        for i in range(len(nums)):
            left = i
            right = (left + nums[i]) % len(nums)
            
            if ((nums[left] > 0 and nums[right] > 0) or (nums[left] < 0 and nums[right] < 0)) and right != left:
                if union(left,right):
                    return True
        
        return False