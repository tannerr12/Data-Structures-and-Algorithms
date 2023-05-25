class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        mono = []
        chunks = 0
        for i in range(len(arr)):
            mono.append(arr[i])
            while mono and mono[-1] <= i:
                mono.pop()
            
            if len(mono) == 0:
                chunks +=1
        
        return chunks