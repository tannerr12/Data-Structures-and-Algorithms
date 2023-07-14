class Solution:
    def minimumPerimeter(self, x: int) -> int:
        

        l, r = 1, 1000000
        while l < r:
            mid = (l + r) // 2
            if (2 * mid) * (mid + 1) * (2 * mid + 1) >= x:
                r = mid
            else:
                l = mid + 1
        return (l * 2) * 4
                