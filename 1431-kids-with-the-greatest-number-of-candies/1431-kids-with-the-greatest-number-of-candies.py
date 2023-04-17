class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        res = []
        
        for num in candies:
            
            res.append(num + extraCandies >= mx)
            
        
        return res