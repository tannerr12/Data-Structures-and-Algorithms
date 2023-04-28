class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        
        numbers = list(set(nums1))
        numbers.sort()
        MOD= 10 ** 9 + 7
        mx = 0
        total = 0
        for i in range(len(nums1)):
            curr = abs(nums1[i] - nums2[i])
            total += curr
            if nums1[i] > nums2[i]:
                val = bisect_left(numbers, nums1[i] - curr)
                if val < len(numbers):
                    mx = max(mx,curr - abs(numbers[val] - nums2[i]))
                if val > 0:
                    mx = max(mx,curr - abs(numbers[val-1] - nums2[i]))
            elif nums1[i] != nums2[i]:
                val = bisect_left(numbers, nums1[i] + curr)
                if val < len(numbers):
                    mx = max(mx,curr - abs(numbers[val] - nums2[i]))
                if val > 0:
                    mx = max(mx,curr - abs(numbers[val-1] - nums2[i]))
            
            
        
        #print(mx)
        
        return (total - mx) % MOD 