class Solution:
    def nextPalindrome(self, num: str) -> str:
        c = Counter(num[:len(num)//2])
        
        l = len(num) // 2
        
        #first swap must be a higher number
        
        #swaps afterwards are always with the lowest number remaining
        
        #can we always find the best first swap?
        
        #its the latest number that has a number > than it
        
        last = 0
        inc = -1
        for i in range(l):
            
            for j in range(int(num[i]) + 1, 10):
                if c[str(j)] > 0:
                    last = i
                    inc = j
                    break

            
            c[num[i]] -= 1
        
        
        
        if inc == -1:
            return ''
        
        c = Counter(num[:len(num)//2])
        ans = []
        
        left = []
        for i in range(last):
            left.append(num[i])
            c[num[i]] -= 1
        
        c[str(inc)] -= 1
        left.append(str(inc))
        right = []
        
        for i in range(10):
            right += [str(i)] * c[str(i)]
        
        #right.sort()
        #print(right)
        
        fullLeft = left + right
        if len(num) % 2 == 0:
            pali = left + right + right[::-1] + left[::-1]
        else:
            pali = left + right + [num[len(num)//2]] + right[::-1] + left[::-1]
        return ''.join(pali)
        
        
        
        
        
                
        "4554"
        "54"
        "5445"