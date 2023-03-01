class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        
        def mergeSort(arr):

            if len(arr) <= 1:
                return arr

            left = mergeSort(arr[:len(arr)//2])

            right = mergeSort(arr[len(arr)//2:])

            leftp,rightp = 0,0

            res = []
            while leftp < len(left) and rightp < len(right):

                

                if left[leftp] < right[rightp]:

                    res.append(left[leftp])
                    leftp+=1

                else:
                    res.append(right[rightp])
                    rightp += 1

            
            res.extend(left[leftp:])
            res.extend(right[rightp:])

            return res


        result = mergeSort(nums)

        return result
    



