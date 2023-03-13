class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        #anything with a self loop should be ignored and any path that connects to it should be ignored
        #if a cycle goes forward anything that goes backwards should be ignored
        #same for negative these need to be seperated
        #a loop must have atleast 1 indegree
        
        parent = [i for i in range(len(nums))]
        def find(val):
            
            if val == parent[val]:
                return val
            
            parent[val] = find(parent[val])
            return parent[val]
        
        
        def union(x,y):
            
            v1,v2 = find(x), find(y)
            
            if v1 != v2:
                parent[v1] = parent[v2]
                return False
            return True
        
        adj = defaultdict(list)
        badLoop = set()
        indegree = set()
        for i in range(len(nums)):

            left = i
            right = (left + nums[i]) % len(nums)
            
            if nums[left] > 0 and nums[right] < 0 or nums[left] < 0 and nums[right] > 0 or right == left:
                badLoop.add(i)
            else:
                pos = 0
                if nums[left] > 0:
                    pos = 1
               # if right in adj and ((nums[right] > 0 and pos) or (nums[right] < 0 and not pos)):
               #     return True
                adj[i].append((right,pos))
                if union(left,right):
                    return True
                indegree.add(right)

        # 0 - > 2 -> 4 - > 6 - > 7
        # 1 - > 3 - > 5 - > 2
        #[2,2,2,2,2,4,7]
        #return False
        #def dfs(i):
            
            
        #print(adj)
        #print(badLoop)
        #res = False
        
        #for key in adj:
        #    if key not in indegree:
        #        continue
            
        #    dfs(key)
            