class Bucket:
    def __init__(self,val):
        self.val = val
        self.next = None

        
class MyHashSet:

    def __init__(self):
        prime = 9679
        self.arr = [Bucket(-1)] * 9679  

    def add(self, key: int) -> None:
        if not self.contains(key):
            newKey = key % 9679 
            b = self.arr[newKey]
            nxt = b.next
            b.next = Bucket(key)
            b.next.next = nxt
        
    def remove(self, key: int) -> None:
      
        newKey = key % 9679 
        b = self.arr[newKey]
        while b.next and b.next.val != key:
            b= b.next

        if b.next and b.next.val == key:
            b.next = b.next.next
            
    def contains(self, key: int) -> bool:
        newKey = key % 9679
        b = self.arr[newKey]
        
        while b:
            if b.val == key:
                return True
            b = b.next
        return False

    
    


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)