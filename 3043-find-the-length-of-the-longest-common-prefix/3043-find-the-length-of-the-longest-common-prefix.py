class trie:
    
    def __init__(self,num):
        
        self.val = num
        self.adj = {}
        

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        t = trie(-1)
        res = 0
        for i in range(len(arr1)):
            
            tri = t
            num = str(arr1[i])
            
            for j in range(len(num)):
                cur = int(num[j])
                
                if cur in tri.adj:
                    tri = tri.adj[cur]
                
                else:
                    tri.adj[cur] = trie(cur)
                    tri = tri.adj[cur]
                
           
               
        
        for i in range(len(arr2)):
            tri = t
            num = str(arr2[i])
            dist = 0
            for j in range(len(num)):
                cur = int(num[j])

                if cur in tri.adj:
                    tri = tri.adj[cur]
                    dist += 1
                else:
                    break

            res = max(res,dist)
        
        return res
        
                
            
            
        