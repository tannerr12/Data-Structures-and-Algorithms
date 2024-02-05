# Definition for an infinite stream.
# class InfiniteStream:
#     def next(self) -> int:
#         pass
class Solution:
    def findPattern(self, stream: Optional['InfiniteStream'], pattern: List[int]) -> int:
        
        arr = []
        while True:
            arr.append(stream.next())
        
            if arr[-len(pattern):] == pattern:
                return len(arr) - len(pattern)
            
     