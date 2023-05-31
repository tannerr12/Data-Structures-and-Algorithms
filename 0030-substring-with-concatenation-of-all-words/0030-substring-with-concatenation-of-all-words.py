class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        mp = set(words)
        ln = len(words[0])
        
        ans = []
        dist = (ln * len(words))
        #print(wordStart)
        worls = Counter(words)

        def slide(pos):
            nonlocal dist
            
            c = defaultdict(int)
            count = 0
            for i in range(pos+ln, pos + dist + 1, ln):
            
                w = s[i-ln:i]
                
                if w in mp:
                    c[w] += 1
                    if c[w] == worls[w]:
                        count +=1
                    elif c[w] > worls[w]:
                        return False
                
            
            if count == len(worls):
                return True

        for i in range(len(s) - dist +1):
            if slide(i):
                ans.append(i)
        
        return ans