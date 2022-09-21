class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        large = ''.join(sorted(map(str, nums), key=LargerNumKey))
 
        return '0' if large[0] == '0' else large
        
        