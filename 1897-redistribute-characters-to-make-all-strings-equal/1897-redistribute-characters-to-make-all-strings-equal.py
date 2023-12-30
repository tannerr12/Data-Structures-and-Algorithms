class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        c = defaultdict(int)
        
        for w in words:
            
            for char in w:
                c[char] += 1
        
        
        for char in c:
            
            if c[char] % len(words) != 0:
                return False
        
        return True