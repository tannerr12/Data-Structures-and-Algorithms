class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        c = defaultdict(int)
        for i in range(len(nums)):
            c[nums[i]] += 1
            
        
        for x,y in zip(moveFrom, moveTo):
            if x == y:
                continue
            c[y] += c[x]
            c[x] = 0
            del c[x]

        #print(c)
        
        return sorted(list(c.keys()))