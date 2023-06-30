class Trie:
    
    def __init__(self, char):
        
        self.char = char
        self.value = 0
        self.adj = {}
        

class MapSum:

    def __init__(self):
        self.tri = Trie('')
        self.seen = {}

    def insert(self, key: str, val: int) -> None:
        oldval = val
        if key in self.seen:
            val = val - self.seen[key]
        self.seen[key] = oldval
        t = self.tri
        
        for char in key:
            t.value += val
            if char in t.adj:
                t = t.adj[char]
            else:
                t.adj[char] = Trie(char)
                t = t.adj[char]
        t.value += val
        

    def sum(self, prefix: str) -> int:
        
        t = self.tri
        
        for char in prefix:
            
            if char in t.adj:
                t = t.adj[char]
            else:
                return 0
        
        return t.value


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)