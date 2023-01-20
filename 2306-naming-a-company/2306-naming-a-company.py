class Solution:
    def distinctNames(self, ideas: List[str]) -> int:

        uchar = set()
        
        wSet = defaultdict(set)
        
        for word in ideas:
            
            head,tail = word[0], word[1:]
            
            uchar.add(head)
            
            wSet[head].add(tail)
            
        res = 0
        n = len(uchar)
        ls = list(uchar)
        for i in range(n):
            si = wSet[ls[i]]
            for j in range(i+1,n):
                sj = wSet[ls[j]]
                
                res += 2 * len(si - sj) * len(sj - si)
        
        
        return res