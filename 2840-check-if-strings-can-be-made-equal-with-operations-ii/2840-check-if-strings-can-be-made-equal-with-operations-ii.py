class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        #all operations should be on the same string
        #just check if the character count of evens and odds are the same between each word
        
        
        even = defaultdict(int)
        odd = defaultdict(int)
        
        for i in range(len(s1)):
            if i % 2:
                odd[s1[i]] += 1
                odd[s2[i]] -= 1
                
            else:
                even[s1[i]] += 1
                even[s2[i]] -= 1
                
        
        for key,val in even.items():
            if val != 0:
                return False
            
        for key,val in odd.items():
            if val != 0:
                return False
        
        return True
                
            