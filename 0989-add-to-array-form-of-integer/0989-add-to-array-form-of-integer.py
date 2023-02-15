class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        carry = 0
        arr = []
        for i in range(len(str(k))):
            
            n = k // (10 ** i) % 10
            val = 0
            if num:
                val = num[-1]
                num.pop()
            else:
                if n + carry >= 10:
                    carry = 1
            
            if n + val + carry < 10:
                arr.append((n + val + carry) % 10)
                carry = 0
            else:
                arr.append((n + val + carry) % 10)
                
            if n + val + carry >= 10:
                carry = 1
                
        
        

        while carry and num:
            
            if num[-1] + carry >= 10:
                arr.append(0)
                num.pop()
            else:
                num[-1] += carry
                carry = 0
        while carry:
            arr.append(carry)
            carry = 0
        arr.reverse()
        return num + arr
            