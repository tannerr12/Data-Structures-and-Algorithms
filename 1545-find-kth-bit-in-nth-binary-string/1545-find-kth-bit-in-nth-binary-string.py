class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def flip(st):
            arr = []
            for i in range(len(st) -1,-1,-1):
                if st[i] == '1':
                    arr.append('0')
                else:
                    arr.append('1')
            
            return ''.join(arr)
        
        start = '0'
        for i in range(1,n):
            
            start = start + "1" + flip(start)
        
        
        return start[k-1]