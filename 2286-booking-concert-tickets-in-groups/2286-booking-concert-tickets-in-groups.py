class SegTree:
    def __init__(self, n, m):
        # make the size even so we have a balance binary tree
        # even idx is left child, odd idx is right child
        self.m = m
        self.size = 2 ** ceil(log(n, 2))
        # copy initial data
        self.maxar = [0] * self.size + [m] * n + [0] * (self.size-n)
        self.sumar = [0] * self.size + [m] * n + [0] * (self.size-n)
    
        # build the 2 segment trees
        for i in range(self.size-1, 0, -1):
            self.maxar[i] = max(self.maxar[i*2], self.maxar[i*2+1])
            self.sumar[i] = self.sumar[i*2] + self.sumar[i*2+1]
        
        self.minRow = self.size # starting from 2nd half, the actual data
        
    def gather(self, req, maxRow):
        # check the max segtree to see if it's possible to get the required seats
        # start from the root of the max tree, index 1
        if self.maxar[1] < req:
            return []
        
        idx = 1
        N = len(self.maxar)
        while idx * 2 < N:
            left, right = idx * 2, idx * 2 + 1
            if left < N and self.maxar[left] >= req: # can find on the left
                idx = left
                continue
            
            if right < N and self.maxar[right] >= req:
                idx = right
                continue
        
        if idx - self.size <= maxRow: # left most index satisfy the boundary
            v = self.maxar[idx]
            self.updateMax(idx, v - req)
            self.updateSum(idx, v - req)
            return [idx - self.size, self.m - v]
        
        return []
    
    def sumq(self, maxRow):
        """
        Return the sum from 0 to maxRow
        """
        l, r = self.size, maxRow + self.size
        result = 0
        while l < r:
            # l is even => left child, can use the value of parent instead
            if l % 2 == 1:
                result += self.sumar[l]
                l += 1
            # r is odd => right child, can use the value of parent instead 
            if r % 2 == 0:
                result += self.sumar[r]
                r -= 1
            l //= 2
            r //= 2
            
        if l == r: # only add once
            result += self.sumar[l]
        
        return result
    
    def update(self, k):
        for row in range(self.minRow, self.size * 2):
            v = self.maxar[row] # original value
            if k > v: # take all
                k -= v
                self.updateMax(row, 0)
                self.updateSum(row, 0)
            else:
                self.updateMax(row, v - k)
                self.updateSum(row, v - k)
                self.minRow = row
                break         
        
        
    def updateMax(self, idx, value):
        self.maxar[idx] = value
        while idx > 1: # root is 1
            idx //= 2
            cur = self.maxar[idx]
            self.maxar[idx] = max(self.maxar[idx*2], self.maxar[idx*2+1])
            if cur == self.maxar[idx]: # no change
                break
            
    def updateSum(self, idx, value):
        self.sumar[idx] = value
        while idx > 1: # root is 1
            idx //= 2
            self.sumar[idx] = self.sumar[idx*2] + self.sumar[idx*2+1]


class BookMyShow:
    def __init__(self, n: int, m: int):
        self.tree = SegTree(n, m)
        
    def gather(self, k: int, maxRow: int) -> List[int]:
        return self.tree.gather(k, maxRow)
        
    def scatter(self, k: int, maxRow: int) -> bool:
        total = self.tree.sumq(maxRow)
        if total >= k: # possible
            self.tree.update(k)
            return True
        
        return False
        


# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)