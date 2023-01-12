class LockingTree:

    def __init__(self, parent: List[int]):
        self.locked = {}
        self.adj = defaultdict(list)
        self.parent = parent
        for i, val in enumerate(parent):
            self.adj[val].append(i)
        
        
    def lock(self, num: int, user: int) -> bool:
        if num not in self.locked:
            self.locked[num] = -1
        if self.locked[num] != -1:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        #print(self.locked)
        if num not in self.locked:
            self.locked[num] = -1
        if self.locked[num] != user:
            return False
        self.locked[num] = -1
        return True
    
    
    def dfs(self,node,user):
        
        total = 0
        for x in self.adj[node]:
            
            total += self.dfs(x,user)
        
        
        if node not in self.locked:
            self.locked[node] = -1
        if self.locked[node] != -1:
            total +=1
        
        self.locked[node] = -1
        return total
    
    
    def upgrade(self, num: int, user: int) -> bool:
        if num not in self.locked:
            self.locked[num] = -1
        if self.locked[num] != -1:
            return False
        
        n = num
        while n != -1:
            n = self.parent[n]
            if n not in self.locked:
                self.locked[n] = -1
            if self.locked[n] != -1:
                return False
        
        unlocked = self.dfs(num,user)
        if unlocked > 0:
            self.lock(num,user)
        return unlocked > 0
        
        
        

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)