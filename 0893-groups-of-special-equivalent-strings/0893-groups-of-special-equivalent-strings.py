class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        mp = defaultdict(int)
        #tuple the size of 52
        for i in range(len(words)):
            a = [0] * 52
            for j in range(len(words[i])):
                char = words[i][j]
                if j % 2 == 0:
                    v = ord(char) - ord('a')
                    a[v] += 1
                else:
                    v = ord(char) - ord('a')
                    v += 26
                    a[v] +=1
            
            mp[tuple(a)] += 1
            
        
        
        return len(mp)
                    
                