class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        #get the numbers divisorts for each number n * sqrt(num)
        #any pairs that do not share any common divisors cannot be swapped
        #as we go through we should know which number needs to be in each postion and compare the 
        #current number to the number that should be there 
        
        parent = defaultdict(int)
        rank = defaultdict(int)
        
        def find(x):
            if x not in parent:
                parent[x] = x
            if x != parent[x]: 
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            
            v1,v2 = find(x),find(y)
            
            if v1 != v2:
                
                if rank[v1] > rank[v2]:
                    parent[v2] = v1
                elif rank[v2] > rank[v1]:
                    parent[v1] = v2
                else:
                    parent[v2] = v1
                    rank[v1] += 1
                return False
            return True
                
        mp = defaultdict(set)
        mpDiv = defaultdict(set)
        for n in set(nums):
            cur = n
            for j in range(2, isqrt(n) + 1):
                
                if cur == 1:
                    break
                
                if cur % j == 0:
                    cur //= j
                    mp[n].add(j)
                    mpDiv[j].add(n)
            
            if cur > 1:
                mp[n].add(cur)
                mpDiv[cur].add(n)
        
        
        
        
        for key1,val1 in mpDiv.items():
            prev = None
            for v in val1:
                if prev == None:
                    prev = v
                    continue
                union(v,prev)
                prev = v
    
        #print(mp)
        #print(mpDiv)
        #sort the divisors
        
        start = sorted(nums)
        #print(start)
        #print(parent)
        for i in range(len(nums)):
            if nums[i] != start[i]:
                x,y = find(nums[i]), find(start[i])
                if x!=y:
                    return False
        
        return True
            
                    
                
            
            
        
        
        