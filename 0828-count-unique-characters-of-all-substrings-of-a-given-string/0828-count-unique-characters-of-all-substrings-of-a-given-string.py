class Solution:
    def uniqueLetterString(self, s: str) -> int:
        
        
        #calculate all of the possible substing combinations from each given index
        #at index 0 how many different unique characters are to the right? A, B, A = 3 AB, BA = 4, ABA = 1
        
        #we cound the number of characters that only appear once
        #maximum of 26 possible points per index 26 * len(s) is possible
        #we should utilize prefix sum in some way
        
        
        prefix= [0] * 26
        mp = defaultdict(lambda:[-1,-1])

    
        res = 0
        last = 0
        for i in range(len(s)):
            cur = ord(s[i]) - ord('A')
            prefix[cur] += 1
            mp[cur][0] = mp[cur][1]
            mp[cur][1] = i
            for j in range(26):
                if prefix[j] == 0:
                    continue
                else:
                    res += mp[j][1] - mp[j][0]

        
        return res
        #A = 1
        #AB = 1, 1
        
        
        
        #1 diff
        #ABA = 2 for b
        #AB = 1 for B 2 for A
        #A = 1 for A
        #= 6
        
        #2 diff
        #ABA = A 2
        #= 2
        #ans = 8
        
        #each character will only have a unique number count from the left most postion 1 time 
        #0s can be ignored
        #we map out each numbers occurance index
        