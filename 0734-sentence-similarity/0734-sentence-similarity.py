class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
                
        if len(sentence1) != len(sentence2):
            return False
        
        
        adj  = defaultdict(set)
        
        for x,y in similarPairs:
            
            adj[x].add(y)
            adj[y].add(x)
            
    
        
        for x,y in zip(sentence1,sentence2):
            
            if x == y or y in adj[x] or x in adj[y]:
                continue
            
            return False
        
        
        return True