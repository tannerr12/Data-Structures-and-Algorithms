class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        merge = []
        q1 = deque()
        q2 = deque()
      
        while word1 or word2:

            if not word2 or (word1 and word1[0] > word2[0]):
        
                merge.append(word1[0])
                word1 = word1[1:]

            elif not word1 or (word2 and word2[0] > word1[0]):
            
                merge.append(word2[0])
                word2 = word2[1:]
            
            else:
                idx = 0
                while idx < len(word1) and idx < len(word2) and word1[idx] == word2[idx]:
                    idx+=1
                
                if idx >= len(word1) and idx >= len(word2):
                    merge.append(word1[0])
                    word1 = word1[1:]
          
                elif idx >= len(word1):
                    merge.append(word2[0])
                    word2 = word2[1:]
                    
                elif idx >= len(word2):
                    merge.append(word1[0])
                    word1 = word1[1:]
                elif word1[idx] > word2[idx]:
                    merge.append(word1[0])
                    word1 = word1[1:]
                else:
                    merge.append(word2[0])
                    word2 = word2[1:]
        

                
        return ''.join(merge)
                