class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one,two = 0,0
        for i in range(len(nums)):
            """
            val = 2
            
            10
            00
            10
            11
            10

            10
            00
            10
            01
            00

            """
            one = (nums[i] ^ one) & ~two
            two = (nums[i] ^ two) & ~one
        

        return one