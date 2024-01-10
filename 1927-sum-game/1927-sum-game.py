class Solution:
    def sumGame(self, num: str) -> bool:
        
        left = num[:len(num)//2]
        right = num[len(num)//2:]
        
        l,r = 0,0
        curr,curl = 0,0
        for i in range(len(left)):
            if left[i] == '?':
                l+=1
            else:
                curl += int(left[i])
        for i in range(len(right)):
            if right[i] == '?':
                r+=1
            else:
                curr += int(right[i])
        
        
        
        #Alice should try to max out left or right
        
        #Alice makes left > right
        score = math.ceil(l/2) * 9
        
        if l % 2 == 1:
            bobRight = math.ceil(r/2) * 9 
        else:
            bobRight = (r//2) * 9
            
        if score + curl > bobRight + curr:
            return True
        
        #Alice maxes right > left
        
        score = math.ceil(r/2) * 9
        if r % 2 == 1:
            bobLeft = math.ceil(l/2) * 9
        else:
            bobLeft = (l // 2) * 9
            
        if curl + bobLeft < curr + score:
            return True
        
       #"93295099"

        
        
        
        
        
        
        