class Solution:
    def queryString(self, s: str, n: int) -> bool:
        
        #0110
        
        #1
        #01
        #11
        #001
        
        
        #just check the max binary combinations by getting Ns rightmost 1
        
        #we need every substring combination of this size
        
        #every substring starts at a leftmost point and ends at a rightmost point of size max N
        
        #for each position in S gather every unique combination of 1s and 0s starting at l and ending at r
        
        #compare it to the number of values between N and 2 ** count(n) - 1?
        
        
        # 7
        
        #001
        #101
        #011
        #111
        
        #001
        #101
        #011
        ns = s[::-1]
        s = ns
        def bintoInt(string):
            num = 0
            for i in range(len(string)):
                if string[i] == '1':
                    num |= (1 << i)
            
            return num
            
        mxN = 0
        for i in range(32,-1,-1):
            if n & (1 << i) > 0:
                mxN = i -1
                break
            
        #print(mxN)
        
        st = set()
        
        for i in range(len(s)):
            #print(s[i:i+mxN + 1])
            #val = int(s[i:i+mxN + 1], 2)
            #print(val)
            if i + mxN < len(s) and s[i+mxN] == '1':
                st.add(s[i:i+mxN + 1])
        
        target = 1
        if mxN > 0:
            target = ((2 ** mxN) - (2 ** (mxN - 1))) + 1
        print(target)
        #print(st)
        if len(st) < target:
            return False
        
        #gap from mxN + 1 -> N
        
        st = set()
        mxN +=1
        for i in range(len(s)):
            val = bintoInt(s[i:i+mxN + 1])
            if i + mxN < len(s) and s[i+mxN] == '1' and val <= n:
                st.add(s[i:i+mxN + 1])
        
        target = n - (2 ** (mxN)) + 1
        #print(target)
        #print(st)
        
        #"10010111100001110010"
        #1000
        #0100 X
        #1100
        #0010
        #1010 X
        #0110 X
        #1110 
        #0001
        #1001 
        #0101
        return len(st) >= target