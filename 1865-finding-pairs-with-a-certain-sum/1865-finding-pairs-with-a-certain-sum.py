class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        
        self.nums1 = Counter(nums1)
        self.nums2 = Counter(nums2)
        self.n2Count = defaultdict(int)
        for i in range(len(nums2)):
            self.n2Count[i] = nums2[i]
        

    def add(self, index: int, val: int) -> None:
        if index in self.n2Count:
            v = self.n2Count[index]
            self.nums2[v] -=1
            v += val
            self.nums2[v] += 1
            self.n2Count[index] = v
        else:
            self.nums2[val] += 1
            self.n2Count[index] = val

    def count(self, tot: int) -> int:
        res = 0
        for key,val in self.nums1.items():
            target = tot - key
            if target in self.nums2:
                res += val * self.nums2[target]
        
        return res
            


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)