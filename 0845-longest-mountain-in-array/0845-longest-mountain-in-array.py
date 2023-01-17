class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        left = [0]        
        cnt = 0
        
        for i in range(1,len(arr)):
            
            if arr[i-1] < arr[i]:
                cnt +=1
                left.append(cnt)
            else:
                cnt = 0
                left.append(cnt)
        
        
        right = [0]        
        cnt = 0
        
        for i in range(len(arr)-2,-1,-1):
            
            if arr[i+1] < arr[i]:
                cnt +=1
                right.append(cnt)
            else:
                cnt = 0
                right.append(cnt)
        
        #print(right)
        right.reverse()
        #print(left)
        #print(right)
        res = 0
        for i in range(len(arr)):
            
            if left[i] > 0 and right[i] > 0:
                res = max(res, left[i] + right[i] + 1)
        
        return res
            