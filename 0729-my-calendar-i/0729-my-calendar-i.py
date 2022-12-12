class SegmentTreeNode:
    def __init__(self,booked=False):
        self.booked = booked
        self.left = self.right = None
        
        
class MyCalendar:
    maxInt = 10**9
    
    def __init__(self):
        self.root = None
    
    def book(self, start: int, end: int) -> bool:
        found = self.search_tree(self.root, 0, self.maxInt, start, end-1)
        if not found:
            self.root = self.insert_tree(self.root, 0, self.maxInt, start, end-1)
            return True
        return False
    
    def search_tree(self, root, lo, hi, start, end):
        if not root or start > end or end<lo or start>hi:
            return False
			
		# lo,hi overlaps with start,end and but the node is fully booked
        if root.booked:
            return True
        mid = lo + (hi-lo)//2
        leftBooked = self.search_tree(root.left, lo, mid, start, min(mid, end))
        rightBooked = self.search_tree(root.right, mid+1, hi, max(start, mid+1), end)
        return leftBooked or rightBooked
        
        
    def insert_tree(self, root, lo, hi, start, end):
        if start > end or end < lo or start > hi:
            return root
        if root==None:
            root = SegmentTreeNode()
        if start <= lo and hi <= end:
            root.booked = True
            return root
        mid = lo + (hi-lo)//2
        root.left = self.insert_tree(root.left, lo, mid, start, min(mid, end))
        root.right = self.insert_tree(root.right, mid+1, hi, max(start, mid+1), end)
        
        # merge operation
        root.booked = root.left and root.left.booked and root.right and root.right.booked
        return root
         