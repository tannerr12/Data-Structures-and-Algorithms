class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        
        #counter hashmap to keep track of the number of numbers that are the same between the two lists
        same = Counter()
        #count the cost for the indexes that are the same between nums1 and nums2
        cost = 0
        #count the number of elements that are the same in nums1 and nums2
        count = 0
        
        for index , (x,y) in enumerate(zip(nums1,nums2)):
            if x == y:
                same[x] +=1
                #has to be moved no matter what
                cost += index
                count +=1
                
        #we have no elements that are the same so we make no swaps
        if len(same) == 0:
            return cost
        
    
        #max by frequency
        key = max(same.keys(), key = lambda x: same[x])
        #most frequent value from hashmap
        t = same[key]
        
 
        #if the max count of same elements is greater than half the size of the list ex [3,3,3,4]
        if t > count - t:
            #this is how many we need to swap out the others will match in some way
            needed = t - (count - t)
            
            for index in range(n):
                #can we swap them out (do not swap with the most frequent element), do not swap elements where the 2 numbers are the same only swap if we need to
                if nums2[index] != key and nums1[index] != nums2[index] and nums1[index] != key and needed > 0:
                    cost += index
                    needed -=1
            if needed > 0:
                return -1
        
        
        return cost