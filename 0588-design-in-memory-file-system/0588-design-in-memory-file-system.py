class Trie:
    
    def __init__(self,directory):
        
        self.directory = directory
        self.adj = {}
        self.content = ''
        
        
class FileSystem:

    def __init__(self):
        self.trie = Trie('/')

    def ls(self, path: str) -> List[str]:
        path = path.split('/')
        t = self.trie
        for i,val in enumerate(path):
            if val in t.adj:
                t = t.adj[val]
            
            if i == len(path) -1:
                if len(t.adj) == 0 and len(t.content) > 0:
                    return [t.directory]
                else:
                    res = []
                    for key in t.adj:
                        res.append(key)
                    
                    res.sort()
                    return res
                    
                

    def mkdir(self, path: str) -> None:
        path = path.split('/')
        t = self.trie
        for val in path:
            if val in t.adj:
                t = t.adj[val]
            else:
                t.adj[val] = Trie(val)
                t = t.adj[val]
        
            

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath.split('/')
        t = self.trie
        for i,val in enumerate(path):
            if val in t.adj:
                t = t.adj[val]

            else:
                t.adj[val] = Trie(val)
                t = t.adj[val]
            
            if i == len(path) -1:
                t.content += content
                
        
            

    def readContentFromFile(self, filePath: str) -> str:
        path = filePath.split('/')
        t = self.trie
        for i,val in enumerate(path):
            if val in t.adj:
                t = t.adj[val]
            
            if i == len(path) -1:
                return t.content
                


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)