class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        merge = []
        q1 = deque()
        q2 = deque()
      
        while word1 or word2:

            if word1 >= word2:
        
                merge.append(word1[0])
                word1 = word1[1:]

            elif word2 > word1:
            
                merge.append(word2[0])
                word2 = word2[1:]

        

                
        return ''.join(merge)
                