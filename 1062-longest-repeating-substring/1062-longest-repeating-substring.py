class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:

        h = defaultdict(int)
        for i in range(len(s)):
            st= s[i]
            h[st] += 1
            for j in range(i+1,len(s)):
                st+=s[j]
                h[st] += 1

        

        #print(h)
        res = 0
        for key,val in h.items():

            if val > 1:
                res = max(res,len(key))


        return res

