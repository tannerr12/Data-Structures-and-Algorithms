from sortedcontainers import SortedList
class RangeModule:
    #solved by merging overlapping intervals in a sorted list by bisecting the leftmost point than popping until we reach and end point and re adding      a single range of the left most to the right most. Removal is done the same but we keep sl.left -> left and right -> sl.right and pop everything      between. As for query range we only need to check the single range since anything between this range will have a minimum gap of 1 so if its not        in this range we can return False.
    def __init__(self):
        self.sl = SortedList()

    def addRange(self, left: int, right: int) -> None:
        #if we have no ranges yet just add than return
        if len(self.sl) == 0:
            self.sl.add([left,right])
            return
        
        #find a range where the end is greater than the left
        lIdx = bisect_left(self.sl,left,key = lambda x: x[1])
        
        #if we are out of bounds on the right or left side just add the range
        if lIdx >= len(self.sl) or right < self.sl[lIdx][0]:
            self.sl.add([left,right])
            return
        
        #grab the leftmost point to re-add later
        start = min(left, self.sl[lIdx][0])
        
        #with end we will eventually grab the last poped ranges end value
        end = right
        while self.sl and lIdx < len(self.sl) and self.sl[lIdx][0] <= right:
            end = max(right, self.sl[lIdx][1])
            #log time removal of range we dont need to update index since the list is shifting left into our index
            self.sl.pop(lIdx)
            
        #re-add our min and max values 
        self.sl.add([start,end])
    
        

    def queryRange(self, left: int, right: int) -> bool:
        #find where our left is less than our end
        lIdx = bisect_left(self.sl,left,key = lambda x: x[1])
        #if the left and right are not within this range return False
        if lIdx < len(self.sl) and self.sl[lIdx][0] <= left and self.sl[lIdx][1] >= right:
            return True
        return False
  
    #same idea as add but we keep track of 2 ranges to re-add
    def removeRange(self, left: int, right: int) -> None:
        #find the point where end > left
        lIdx = bisect_left(self.sl,left,key = lambda x: x[1])
        #if we are out of bounds on either side we can exit early
        if lIdx >= len(self.sl) or right < self.sl[lIdx][0]:
            return 
        #gather our first start and end for our left range
        #start -> left
        start = self.sl[lIdx][0]
    
        #gather our point for our end range
        e=self.sl[lIdx][1]    
        self.sl.pop(lIdx)
        #our update to end is just there to get the last point before popping and exiting
        while self.sl and lIdx < len(self.sl) and self.sl[lIdx][0] <= right:
            e = self.sl[lIdx][1]
            self.sl.pop(lIdx)
            
        #start range
        if start < left:
            self.sl.add([start, left ])
        #end range
        if right < e:
            self.sl.add([right, e])
        
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)