class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        c = Counter(nums)
        res = 0
        for key in list(c):
            if key == k - key:
                res += c[key] // 2
                c[key] = 0
            else:
                am = min(c[key], c[k - key])
                res += am

                c[key] -= am
                c[k - key] -= am
        
        return res
            