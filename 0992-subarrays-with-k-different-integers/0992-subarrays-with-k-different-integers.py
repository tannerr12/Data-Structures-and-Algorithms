class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def findK(k):
            l = 0
            res = 0 
            uni = {}

            for i in range(len(nums)):

                if nums[i] in uni:
                    uni[nums[i]] +=1
                else:
                    uni[nums[i]] = 1

                while len(uni) > k:

                    uni[nums[l]] -=1

                    if uni[nums[l]] == 0:
                        del uni[nums[l]]
                    l+=1

                res += i - l +1

            return res
        
        return findK(k) - findK(k-1)
                