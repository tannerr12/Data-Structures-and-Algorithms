class TodoList:

    def __init__(self):
        self.mp = defaultdict(lambda:defaultdict(list))
        self.ids = 1
        self.completed = set()
    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:

        self.mp[userId][''].append([dueDate,taskDescription,self.ids])
        for val in set(tags):
            self.mp[userId][val].append([dueDate,taskDescription,self.ids])
        
        self.ids += 1
        return self.ids -1

    def getAllTasks(self, userId: int) -> List[str]:
        if userId not in self.mp:
            return []
        

        ans = []
        #print(userId)
        
        #print(self.mp[userId][''])
        for x,y,z in sorted(self.mp[userId]['']):
            if (userId, z) in self.completed:
                continue
            ans.append(y)
        
        return ans
            

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        
        ans = []
        #print(self.mp[userId][tag])
        for x,y,z in sorted(self.mp[userId][tag]):
            if (userId, z) in self.completed:
                continue
            ans.append(y)
            
        return ans

    def completeTask(self, userId: int, taskId: int) -> None:
        self.completed.add((userId, taskId))
        


# Your TodoList object will be instantiated and called as such:
# obj = TodoList()
# param_1 = obj.addTask(userId,taskDescription,dueDate,tags)
# param_2 = obj.getAllTasks(userId)
# param_3 = obj.getTasksForTag(userId,tag)
# obj.completeTask(userId,taskId)