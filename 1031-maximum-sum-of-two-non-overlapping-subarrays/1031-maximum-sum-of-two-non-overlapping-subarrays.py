class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        
        curFirst = 0
        curSecond = 0
        l = 0
        l2 = 0
        res = 0
        for i in range(len(nums)):
            
            curFirst += nums[i]
            
            if i - l + 1 == max(firstLen, secondLen):
                l2 = i + 1
                curSecond=0
                if len(nums) - i >= min(firstLen, secondLen):
                    for j in range(i+1, len(nums)):
                        curSecond += nums[j]

                        while j - l2 + 1 > min(firstLen, secondLen):
                            curSecond -= nums[l2]
                            l2 +=1

                        if j - l2 + 1 ==  min(firstLen, secondLen):
                            res = max(res, curSecond + curFirst)

                l2 = 0
                curSecond=0
                if l >= min(firstLen, secondLen):
                    for j in range(0, l):
                        curSecond += nums[j]

                        while j - l2 + 1 > min(firstLen, secondLen):
                            curSecond -= nums[l2]
                            l2 +=1

                        if j - l2 + 1 ==  min(firstLen, secondLen):
                            res = max(res, curSecond + curFirst)

                curFirst -= nums[l]
                l+=1
        
        
        return res