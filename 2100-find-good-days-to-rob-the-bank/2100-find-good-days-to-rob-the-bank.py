class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        prefix = []
        stack = deque()
        
        for i in range(len(security)):
            
            
                
            if stack and security[i] > stack[-1]:
                stack = deque()
            if len(stack) == time +1:
                stack.popleft()
            stack.append(security[i])
                #prefix.append(security[i])
        
            prefix.append(len(stack) == time +1)
            
        
        postfix = []
        stackPost = deque()
        for i in range(len(security)-1,-1,-1):

            if stackPost and security[i] > stackPost[-1]:
                stackPost = deque()
            if len(stackPost) == time +1:
                stackPost.popleft()
            stackPost.append(security[i])
                #prefix.append(security[i])
        
            postfix.append(len(stackPost) == time +1)
            
        #print(prefix)
        #print(postfix)
        
        res = []
        for i,v in enumerate(security):
            
            #check if good day
            if prefix[i] and postfix[-(i +1)]:
                res.append(i)
        
        
        return res