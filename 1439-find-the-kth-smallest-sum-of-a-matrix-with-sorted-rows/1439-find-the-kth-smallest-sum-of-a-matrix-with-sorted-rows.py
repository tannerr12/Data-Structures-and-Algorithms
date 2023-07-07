class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        
        heap = []
        
        seen = set()
        heappush(heap, (sum(mat[i][0] for i in range(len(mat))), [0] * len(mat)))
        
        
        while k:
            
            cost, arr = heappop(heap)
            
            #seen.add(tuple(arr))
            
            k-=1
            if k == 0:
                return cost
            for i in range(len(mat)):
                if arr[i] < len(mat[i]) -1:
                    newCost, newArr = cost, arr.copy()
                    newArr[i] += 1
                    newCost -= mat[i][newArr[i] -1]
                    newCost += mat[i][newArr[i]]

                    if tuple(newArr) in seen:
                        continue
                    seen.add(tuple(newArr))
                    heappush(heap, (newCost, newArr))
                
                
        
        return cost
        