class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        
        flowers.sort()
        
        N = len(flowers)
        
        if flowers[0] >= target:
            return full * N
        
        
        prefix = [0]
        for x in flowers:
            prefix.append(prefix[-1] + x)
            
        
        def go(leftover, rightBound):
            
            if rightBound < 0:
                return 0
            left = 0
            right = rightBound
            
            while left < right:
                
                mid = (left + right) //2
                #find the average after adding leftover if the right value is less than the average search right further
                if (prefix[mid + 1] + leftover) // (mid + 1) >= flowers[mid + 1]:
                    left = mid + 1
                else:
                    right = mid
            #return the best average or the target -1 since thats the partials highest value
            return min((prefix[left + 1] + leftover) // (left + 1), target -1)
        
        #no full flowers
        best = go(newFlowers, N-1) * partial 
        
        for right in range(N-1,-1,-1):
            #cost to make full
            delta = max(target - flowers[right], 0)
            newFlowers -= delta
            
            #out of full options
            if newFlowers < 0:
                break
            
            #find best partial to the left
            partialMin = go(newFlowers, right - 1)
                
            fullCount = N - right
            best = max(best, fullCount * full + partial * partialMin)
        
        return best