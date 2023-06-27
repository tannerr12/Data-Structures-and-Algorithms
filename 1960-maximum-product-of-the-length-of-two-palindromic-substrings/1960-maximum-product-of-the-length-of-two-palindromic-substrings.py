class Solution:
    def maxProduct(self, s: str) -> int:
        def manacher(s):
            #Manachers algorithm to get palindrones in O(N)
            sl = '#'.join('^{}$'.format(s))
            C,R = 0,0
            P = [0] * len(sl)
            for i in range(1,len(sl)-1):

                mirror = C * 2 - i

                if R > i:
                    P[i] = min(R - i, P[mirror])


                while sl[i + 1 + P[i]] == sl[i - 1 - P[i]]:
                    P[i] +=1


                if (i + P[i]) > R:
                    R = i + P[i]
                    C = i


            return P[2:-2:2]
        
        n = len(s)
        m = manacher(s)
        
        left = [1] * n
        
        #mark the ending for longest palindrone
        for i in range(n):
            r = i + (m[i] -1) //2
            left[r] = max(left[r], m[i])
        
        
        #update the shorter pal based on the longest one
        
        for i in range(n-2,-1,-1):
            left[i] = max(left[i], left[i+1] -2)
        
        #get the max from length from all pal on the left
        for i in range(1,n):
            left[i] = max(left[i], left[i-1])
        
        
        right = [1] * n
        #mark the ending for longest palindrone
        for i in range(n-1,-1,-1):
            l = i - (m[i] -1) //2
            right[l] = max(right[l], m[i])
        
        
        #update the shorter pal based on the longest one
        
        for i in range(1,n):
            right[i] = max(right[i], right[i-1] -2)
        
        #get the max from length from all pal on the right
        for i in range(n-2,-1,-1):
            right[i] = max(right[i], right[i+1])
        
        
        #line sweep each index
        ans = 0
        for i in range(n-1):
            ans = max(ans,left[i] * right[i+1])
        
        
        return ans

        
        
        
        
            
            