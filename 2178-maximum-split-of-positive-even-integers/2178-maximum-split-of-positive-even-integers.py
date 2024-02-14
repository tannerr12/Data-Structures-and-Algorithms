class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        
        
        if finalSum % 2:
            return []
        ans = []
        num = 2
        while num + num + 2 <= finalSum:
            finalSum -= num
            ans.append(num)
            num += 2
        
        ans.append(finalSum)
        return ans