class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        ans = []
        
        idx1,idx2,idx3 = 0,0,0
        
        while idx1 < len(arr1) and idx2 < len(arr2) and idx3 < len(arr3):
            mn = min(arr1[idx1], arr2[idx2], arr3[idx3])
            if arr1[idx1] == arr2[idx2] == arr3[idx3]:
                ans.append(arr1[idx1])
                
                while idx1 < len(arr1) and arr1[idx1] == ans[-1]:
                    idx1 += 1
                    
                while idx2 < len(arr2) and arr2[idx2] == ans[-1]:
                    idx2 += 1
                    
                while idx3 < len(arr3) and arr3[idx3] == ans[-1]:
                    idx3 += 1
                    
            
            while idx1 < len(arr1) and arr1[idx1] == mn:
                idx1 += 1

            while idx2 < len(arr2) and arr2[idx2] == mn:
                idx2 += 1

            while idx3 < len(arr3) and arr3[idx3] == mn:
                idx3 += 1
                    
    
    
        return ans