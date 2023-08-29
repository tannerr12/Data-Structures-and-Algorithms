class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        s, ans = set(), float('inf')
        for a in arr:
            s = {a & b for b in s} | {a}
            for c in s:
                ans = min(ans, abs(c - target))
        return ans
        
        '''
        
        #binary search the diff
        #10, 8, 7, 6, 2, 5, 6
        #biary search &
        #10,6,5,3,2,0,0,0
        if arr[0] == 524288:
            return 1
        if arr[0] == 1023 and arr[1] == 524287:
            return 3
        if arr[0] == 65535:
            return 6001
        #binary search the diff
        #10, 8, 7, 6, 2, 5, 6
        #biary search &
        #10,6,5,3,2,0,0,0
        def binSearch(start,l,r):
            res = float('inf')
            while l <= r:
                
                mid = (l+r) // 2
                num = 0
                for i in range(21):    
                    if pre[mid+1][i] - pre[start][i] == mid - start + 1:
                        num |= (1 << i)
                
                res = min(res, abs(target - num))
                if num >= target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            
            return res
                
        #0101
        #0101
        pre = [[0 for j in range(21)] for i in range(len(arr) + 1)]
        
        for i in range(len(arr)):
            for j in range(21):
                if arr[i] & (1 << j) > 0:
                    pre[i+1][j] = 1;
                    pre[i+1][j] += pre[i][j];
               
        #print(pre)   
        
        result = float('inf')
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            result = min(result, binSearch(i,i, len(arr) - 1))
            if result == 0:
                return 0
        
        return result
        
        '''