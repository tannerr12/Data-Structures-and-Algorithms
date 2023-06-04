class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.mp = defaultdict(list)
        
        for i,val in enumerate(arr):
            self.mp[val].append(i)
        
    def query(self, left: int, right: int, val: int) -> int:
        
        if len(self.mp[val]) == 0:
            return 0
        
        else:
            l = bisect_left(self.mp[val],left)
            r = bisect_right(self.mp[val], right)
            
            return r - l
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)