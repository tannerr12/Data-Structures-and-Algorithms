class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        #anything with a self loop should be ignored and any path that connects to it should be ignored
        #if a cycle goes forward anything that goes backwards should be ignored
        #same for negative these need to be seperated
        #a loop must have atleast 1 indegree
        
        
        #with these observations we can assume that anything that passes all of these checks and reconnects with 
        #another node of its same cycle is infact a valid loop since it would be of atleast size 2
        
        #implement union find
        parent = [i for i in range(len(nums))]
        rank = [0] * len(nums)
        
        #find with compression
        def find(val):
            if val == parent[val]:
                return val
            parent[val] = find(parent[val])
            return parent[val]
        
        #union with rank
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
        
        #loop over all of nums and check the current value and the target value. 
        #if they are not both positive or both negative or we see a self cycle this connection should be ignored
        for i in range(len(nums)):
            left = i
            right = (left + nums[i]) % len(nums)
            if ((nums[left] > 0 and nums[right] > 0) or (nums[left] < 0 and nums[right] < 0)) and right != left:
                #if true we found a relationship
                if union(left,right):
                    return True
                
        #no relationship found
        return False