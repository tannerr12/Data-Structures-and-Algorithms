class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        
        
        #can we group values by their % k position
        #each group will need the minimum moves to make sorted
        #groups do not affect eachother
        
        
        groups = defaultdict(list)
        
        
        for i in range(len(arr)):
            
            groups[i % k].append(arr[i])
            
        
        #4,2
        #2,4
        
        
        #[12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3]
        #12,12,14,17,18
        def lengthOfLIS(nums):

            sub = []

            for num in nums:

                i = bisect_right(sub, num)


                if i >= len(sub):
                    sub.append(num)

                else:
                    sub[i] = num
        
        
            return len(sub)
        
        res = 0
        for group in groups.values():
            
            res += len(group) - lengthOfLIS(group)
            
        
        
        return res
            