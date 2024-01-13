class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        #always take the largest 2 numbers from the end on the left side
        #always take the smallest 2 numbers on the start on the right side
        
        
        intervals.sort(key=lambda x:(x[1], -x[0]))
        
        res = 0
        largest = -1
        second = -1
        
        for i in range(len(intervals)):
            a,b = intervals[i]
            
            #check if there inside the range
            largestIn = (a <= largest)
            secondIn = (a <= second)
            
            #there both inside the range
            if largestIn and secondIn:
                continue
            
            #neither of them are inside the range
            res += 1 + (not largestIn)
            
            if largestIn:
                second = largest
            else:
                #second from the end
                second = b - 1
            
            #set to the end
            largest = b
        
        return res
            
            
            
            
            

                    
        