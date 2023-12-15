class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        
        c1 = Counter(a)
        c2 = Counter(b)
        res = float('inf')
        for key in sorted(c1):

            for key2 in sorted(c2):

                #change every letter in c2 to key2
                cost1 = len(b) - c2[key2]
                #change every letter in c1 to key
                cost2 = len(a) - c1[key]
                
                res = min(res, cost1 + cost2)
        
        arr1 = []
        arr2 = []
        
        for char in a:
            val = ord(char) - ord('a')
            arr1.append(val)
        
        for char in b:
            val = ord(char) - ord('a')
            arr2.append(val)
        
        
        arr1.sort()
        arr2.sort()
        
        #print(arr1)
        #print(arr2)
        
        for i in range(26):
            #left a + right b
            idx1 = bisect_left(arr1, i)
            idx2 = bisect_left(arr2, i)
            extra = 0
            if i == 0:
                extra = c1['a']
            res = min(res, idx1 + len(arr2) - idx2 + extra)
            #right a + left b
            idx1 = bisect_right(arr1, i)
            idx2 = bisect_right(arr2, i)
            extra = 0
            if i == 25:
                extra = c1['z']
            res = min(res, len(arr1) - idx1 + idx2 + extra)
            
        return res
                
                