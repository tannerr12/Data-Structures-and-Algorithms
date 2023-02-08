class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        c = Counter(nums)
        
        end = defaultdict(int)
        
        
        for i,n in enumerate(nums):
            
            if c[n] > 0:
                c[n] -=1
                if end[n-1] > 0:
                    end[n-1] -=1
                    end[n] += 1
                
                else:
                    if c[n+1] and c[n+2]:
                        c[n+1] -=1
                        c[n+2] -=1
                        end[n+2] +=1
                        
                        
                    else:
                        return False
        
        return True
        
        
        
        
        
        