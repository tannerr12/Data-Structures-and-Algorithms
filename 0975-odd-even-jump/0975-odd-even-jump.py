from sortedcontainers import SortedList

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        sl = SortedList([[arr[-1], len(arr)-1]])
        dp = [[False,False] for j in range(len(arr))]
        
        dp[-1] = [True,True]
        
       # minSeen = [arr[-1],len(arr)-1]
       # maxSeen = [arr[-1],len(arr)-1]
        
        for i in range(len(arr)-2,-1,-1):
            nxtMin = bisect_left(sl,arr[i],key=lambda i: i[0])
            if nxtMin < len(sl) and sl[nxtMin][0] >= arr[i]:
                
                dp[i][0] = dp[sl[nxtMin][1]][1]
            
            if nxtMin >= len(sl) or sl[nxtMin][0] > arr[i]:
                nxtMin -=1
                if nxtMin > 0:
                    nxtMin = bisect_left(sl,sl[nxtMin][0],key=lambda i: i[0])
            if nxtMin >= 0 and sl[nxtMin][0] <= arr[i]:
                dp[i][1] = dp[sl[nxtMin][1]][0]
            
            sl.add([arr[i],i])
        #print(dp)
        
        res = 0
        for x,y in dp:
            if x:
                res +=1
        
        return res
                
                
            
            