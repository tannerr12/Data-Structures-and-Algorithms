class seg_tree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [(0, -1)]*self.n+[(1, n) for n in nums]  # (freq, number)
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.merge(self.tree[i*2], self.tree[i*2+1])
    
    def merge(self, a, b):
        _, x = max(a, b)
        return (a[0]+b[0], x) if a[1]==b[1] else (abs(a[0]-b[0]), x)
    
    def st_query(self, l, r):
        l, r, x = l+self.n, r+self.n, (0, -1)
        while(l<r):
            if l%2:
                x = self.merge(self.tree[l], x)
                l += 1
            if r%2:
                r -= 1
                x = self.merge(self.tree[r], x)
            l //= 2
            r //= 2
        return x

    
    
    
class MajorityChecker:
    

    def __init__(self, arr):
        self.seg, self.idx_mp = seg_tree(arr), defaultdict(list)
        for i in range(len(arr)):
            self.idx_mp[arr[i]].append(i)
	
    def query(self, l, r, x):
        n = self.seg.st_query(l, r+1)[1]
        if n==-1:
            return -1
        i = bisect.bisect_left(self.idx_mp[n], l) 
        j = bisect.bisect(self.idx_mp[n], r)
        return n if j - i >= x else -1    


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)