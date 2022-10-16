class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #nums = list(s)
        h = Counter(s)
        
        #alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
        stack = []
        seen = set()
        for i in range(len(s)):
            
            #if not stack or ord(nums[i]) > stack[-1] and nums[i] not in stack:
             #   stack.append(nums[i])
            h[s[i]] -=1
            while stack and ord(s[i]) < ord(stack[-1]) and h[stack[-1]] != 0 and s[i] not in seen:
                v = stack.pop()
                seen.remove(v)
            
            
            if s[i] not in seen:
                stack.append(s[i])
                seen.add(s[i])
            
            
            
            
            
        
        return ''.join(stack)