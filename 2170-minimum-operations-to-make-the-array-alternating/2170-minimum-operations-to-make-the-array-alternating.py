class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        count = defaultdict(int)
        for i in range(0,len(nums),2):
            count[nums[i]] += 1
        
        #print(count)
        
        count2 = defaultdict(int)
        for i in range(1,len(nums),2):
            count2[nums[i]] += 1
            
        
        b1,b2 = [0,0], [0,0]
        
        for key,val in count.items():
            if val >= b1[0]:
                b2 = b1
                b1 = [val, key]
            elif val >= b2[0]:
                b2 = [val,key]
                
        c1,c2 = [0,0], [0,0]
        
        for key,val in count2.items():
            if val >= c1[0]:
                c2 = c1
                c1 = [val, key]
            elif val >= c2[0]:
                c2 = [val,key]
                
        if c1[1] != b1[1]:
            return len(nums) - c1[0] - b1[0]
        
        else:
            return len(nums) - max(c1[0] + b2[0], b1[0] + c2[0])