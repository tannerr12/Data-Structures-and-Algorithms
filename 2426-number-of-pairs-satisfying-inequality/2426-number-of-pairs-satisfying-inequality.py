from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
     
    
        nums = []

        for x,y in zip(nums1,nums2):
            nums.append(x-y)



        def merge(nums):

            if len(nums) <= 1:
                return nums

            left = merge(nums[:len(nums)//2])

            right = merge(nums[len(nums)//2:])

            return sort(left,right)

        res = 0
        def sort(left,right):
            nonlocal res
            l,r = 0,0

            arr = []

            j = 0

            for i in range(len(right)):

                while j < len(left) and right[i] + diff >= left[j]:
                    j+=1


                res += j

            while l < len(left) and r < len(right):

                if left[l] <= right[r]:
                    arr.append(left[l])
                    l+=1

                else:
                    arr.append(right[r])
                    r+=1



            arr.extend(left[l:])
            arr.extend(right[r:])

            return arr



        merge(nums)
        return res