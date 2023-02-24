class MyHashMap:

    def __init__(self):
        self.arr = [[]] * 1000
        
    def put(self, key: int, value: int) -> None:
        newKey = key % 1000
        if not self.hasKey(key):
           
            self.arr[newKey].append([key,value])
        else:
            
            for i,[k,v] in enumerate(self.arr[newKey]):
                if k == key:
                    self.arr[newKey][i][1] = value
                    
    
    def get(self, key: int) -> int:
        newkey = key % 1000
        #print(self.arr[newkey])
        for k,v in self.arr[newkey]:
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        newKey = key % 1000
        
        for i in range(len(self.arr[newKey])):
            if self.arr[newKey][i][0] == key:
                self.arr[newKey].pop(i)
                return
    
    def hasKey(self, key):
        newKey = key % 1000
   
        for k,val in self.arr[newKey]:
            if k == key:
                return True
        
        return False


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)