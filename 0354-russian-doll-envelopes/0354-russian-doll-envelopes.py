class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        #lis options
        envelopes = sorted(envelopes, key=lambda x:(x[0], -x[1]))
        sub = []

        for num in envelopes:
            w,l = num
            i = bisect_left(sub, l)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(l)
              
            
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = l
              
           
    
        
                
        return len(sub)

                
                
        