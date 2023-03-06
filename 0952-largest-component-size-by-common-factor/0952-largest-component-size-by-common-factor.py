class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        #union find + prime factorization
        N = len(nums)
        parent = [i for i in range(N)]
        rank = [0] * N
        def find(val):
            
            if val == parent[val]:
                return val
            
            parent[val] = find(parent[val])
            return parent[val]
        
        
        def union(x,y):
            
            v1,v2 = find(x),find(y)
            
            
            if v1 != v2:
                
                if rank[v1] > rank[v2]:
                    parent[v2] = v1
                
                elif rank[v2] > rank[v1]:
                    parent[v1] = v2
                    
                else:
                    parent[v2] = v1
                    rank[v1] +=1
                    
                return True
            return False
        
        
        factMap = {}
        for i,num in enumerate(nums):
            n = num
            j = 2
            while j < int(sqrt(num))+1 and n != 1:
                
                if n % j == 0:
                    #we are a factor
                    if j in factMap:
                        union(factMap[j], i)
                    factMap[j] = i
                
                while n % j == 0:
                    n //= j
                
                j += 1 + j % 2
            #we are a large prime
            if n > 1:
                if n in factMap:
                    union(factMap[n], i)
                factMap[n] = i
            
        #print(factMap)
        #print(parent)
        for i in range(len(nums)):
            find(i)
        count = Counter(parent)
        return max(count.values())