class Solution:
    def findIndices(self, nums: List[int], idd: int, vd: int) -> List[int]:
        
        if idd == 0 and vd == 0:
            return [0,0]
        
        mxmn = defaultdict(lambda:[float('inf'),-1,float('-inf'),-1])
    
        for i in range(len(nums) -1, -1, -1):
            if nums[i] < mxmn[i+1][0]:
                mxmn[i][0] = nums[i]
                mxmn[i][1] = i
            else:
                mxmn[i][0] = mxmn[i+1][0]
                mxmn[i][1] = mxmn[i+1][1]
                
            if nums[i] > mxmn[i+1][2]:
                mxmn[i][2] = nums[i]
                mxmn[i][3] = i
            else:
                mxmn[i][2] = mxmn[i+1][2]
                mxmn[i][3] = mxmn[i+1][3]
        
        for i in range(len(nums)  - idd):
            
            n = nums[i]
            mx = mxmn[i+idd][2]
            mn = mxmn[i+idd][0]
            if abs(n - mx) >= vd:
                return [i, mxmn[i+idd][3]]
            elif abs(n - mn) >= vd:
                return [i, mxmn[i+idd][1]]
        
        
        return [-1,-1]