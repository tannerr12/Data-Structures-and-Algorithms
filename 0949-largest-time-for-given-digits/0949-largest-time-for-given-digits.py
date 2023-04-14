class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        
        res = [0] * 5
        c = Counter(arr)
        great5 = 0
        for key in c:
            if key > 5:
                great5 += c[key]
                
        #set the size of the ranges for each position
        cycl = {0:3, 1:4, 2:0,3:6,4:10}
        
        #O(1)
        for i in range(5):
            #spacer
            if i == 2:
                continue
            assigned = False
            
            #edge case
            #we were allowed to take 2 so fill the second slot in with the largest number we have remaining
            if i == 1 and int(res[0]) < 2:
                #4 at most
                mx = max(c)
                res[i] = str(mx)
                c[mx] -=1
                if c[mx] == 0:
                    del c[mx]
                continue
                
            #try all number ranges for the given postion and take the largest
            for j in range(cycl[i] -1,-1,-1):
                #edge case
                #if there are more than 2 numbers greater than 5 in the list than we cant take 2 as the first number since we will need it in the second position
                if i == 0 and j == 2 and great5 >= 2:
                    continue
                
                #if we have this number remaining use it and remove it from our dict
                if j in c:
                    assigned = True
                    res[i] = str(j)
                    c[j] -=1
                    if c[j] == 0:
                        del c[j]
                    break
            
            #we could not assign this position
            if not assigned:
                return ""
        
        res[2] = ":"
        return ''.join(res)
