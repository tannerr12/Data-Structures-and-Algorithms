from sortedcontainers import SortedList

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        
        #get next higher and next lower
        #same idea here but instead of a sorted list we use a monotonic stack to get the next greater element and the next 
        #lower element
        #we sort by the values in the list keeping track of their index than when we hit a value where i is > than the top of the stack we
        #can assign the index
        higher = [0] * len(arr)
        lower = [0] * len(arr)

        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(arr)):
            
            while stack and stack[-1] < i:
                higher[stack.pop()] = i
            
            stack.append(i)
        for a, i in sorted([-a, i] for i, a in enumerate(arr)):
            
            while stack and stack[-1] < i:
                lower[stack.pop()] = i
            
            stack.append(i)
        
        dp = [[False,False] for j in range(len(arr))]
        dp[-1] = [True,True]
        
        #since we already know higher and lower this becomes simple
        for i in range(len(arr)-2,-1,-1):
           
            dp[i][0] = dp[higher[i]][1]
            dp[i][1] = dp[lower[i]][0]
            
         
        #print(dp)
        res = 0
        for x,y in dp:
            if x:
                res +=1
        
        return res
        
        """
            
        sl = SortedList([[arr[-1], len(arr)-1]])
        dp = [[False,False] for j in range(len(arr))]
        
        dp[-1] = [True,True]

        
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
        """
                
                
            
            