class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        
        res = [1] * len(ratings)
        stack = []
        for i in range(len(ratings)):
            
            if stack and ratings[stack[-1]] <= ratings[i]:
                candy = 0
        
                while stack:
                    
                    val = stack.pop()
                    candy +=1
                    res[val] = candy

                    if len(stack) == 0 and val > 0:
                        if ratings[val -1] == ratings[val]:
                            c = 1
                        else:
                            c = res[val-1] + 1
                        
                        res[val] = max(res[val], c)
                
            stack.append(i)
        
        
        
        candy = 0
      
        while stack:
            val = stack.pop()

            candy +=1
            res[val] = candy

            if len(stack) == 0 and val > 0:
                if ratings[val -1] == ratings[val]:
                    c = 1
                else:
                    c = res[val-1] + 1

                res[val] = max(res[val], c)
        
        
        return sum(res)
                    
                    