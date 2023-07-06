class Trie:
    
    def __init__(self,val):
        
        self.val = val
        self.adj = {}
        self.res = -1

class FileSystem:

    def __init__(self):
        self.tri = Trie('')

    def createPath(self, path: str, value: int) -> bool:
        t = self.tri
        p = path.split('/')[1:]
        res = False
        for i in range(len(p)):
            if p[i] in t.adj:
                t = t.adj[p[i]]
            else:
                if i == len(p)-1:   
                    t.adj[p[i]] = Trie(p[i])
                    t = t.adj[p[i]]
                    res = True
                else:
                    return False
        
        if res:
            t.res = value
        return res
        

    def get(self, path: str) -> int:
        t = self.tri
        p = path.split('/')[1:]
        for i in range(len(p)):
            if p[i] in t.adj:
                t = t.adj[p[i]]
            else:
                return -1
        
        return t.res

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)