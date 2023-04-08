class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
        parent = [i for i in range(max(arr))]
        rank = [0] * max(arr)
        size = [0] * max(arr)
        bits = [0] * max(arr)
        
        count = 0
        def find(val):
            
            if parent[val] == val:
                return val
            
            parent[val] = find(parent[val])
            
            return parent[val]
            
        def union(x,y):
            nonlocal count
            v1,v2 = find(x),find(y)
            
            if v1 != v2:
                
                if rank[v1] > rank[v2]:
                    if size[v1] == m:
                        count -=1
                    if size[v2] == m:
                        count -=1
                    size[v1] += size[v2]
                    if size[v1] == m:
                        count +=1
                    parent[v2] = v1
                elif rank[v2] > rank[v1]:
                    if size[v1] == m:
                        count -=1
                    if size[v2] == m:
                        count -=1
                        
                    size[v2] += size[v1]
                    if size[v2] == m:
                        count +=1
                        
                    parent[v1] = v2
                else:
                    if size[v1] == m:
                        count -=1
                    if size[v2] == m:
                        count -=1
                    size[v1] += size[v2]
                    if size[v1] == m:
                        count +=1
                    parent[v2] = v1
                    rank[v1] +=1
                    
                return False
            return True
        
        
        bits = [0] * len(arr)
        res = -1
        for i, val in enumerate(arr):
            val = val -1
            #check left and right and add + merge each group
            left,right = None,None
            if val > 0:
                left = val -1
            if val < len(size) -1:
                right = val + 1
            
            bits[val] = 1
            size[val] = 1
            if m == 1:
                count +=1
            if left is not None and right is not None and bits[left] and bits[right]:
                union(val,left)
                union(val,right)
            elif left is not None and bits[left]:
                union(val,left)
            elif right is not None and bits[right]:
                union(val,right)
            
            
        
            if count > 0:
                res = i + 1
            #print(i +1)
            #print(size)
            #print(bits)
                
        return res