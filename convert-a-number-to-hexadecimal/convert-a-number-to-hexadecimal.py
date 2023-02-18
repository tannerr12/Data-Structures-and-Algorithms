class Solution:
    def toHex(self, num: int) -> str:
        

        #1-10 A-F = 16
        #24
        #011010
        h = {10:'a', 11:'b',12:'c', 13:'d',14:'e', 15:'f'}

        res = ''
        while True:

            x,y = divmod(num,16)
            y = (num / 16) % 1
            num = x
            val = y * 16
            if val in h:
                res = h[val] + res
            else:
                res = str(int(val)) + res
            if x == 0 or len(res) == 8:
                break
        return res