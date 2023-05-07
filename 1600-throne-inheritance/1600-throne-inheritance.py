class ThroneInheritance:

    def __init__(self, kingName: str):
        self.mp = defaultdict(list)
        self.dead = set()
        self.order = []
        self.mp[kingName] = []
        self.kingName = kingName
    def birth(self, parentName: str, childName: str) -> None:
        self.mp[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.order = []
        self.dfs(self.kingName)
        return self.order

    
    
    def dfs(self, node):
        
        if node not in self.dead:
            self.order.append(node)
            
        for val in self.mp[node]:
            self.dfs(val)
        
    
        
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()