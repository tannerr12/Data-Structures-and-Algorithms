class Solution:

    def __init__(self, nums: List[int]):
        self.mp = defaultdict(list)
        
        for i,val in enumerate(nums):
            self.mp[nums[i]].append(i)
        

    def pick(self, target: int) -> int:
        idx = random.randint(0, len(self.mp[target])-1)
        return self.mp[target][idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)