class Solution:
    def isHappy(self, n: int) -> bool:
        ns = str(n)
        check = set()
        while ns != "1":
            total = 0
            for char in ns:
                total += int(char) **2
            if total in check:
                return False
            check.add(total)
            ns = str(total)
        
        
        return True
                