class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        #keep track of the difference between characters than hashmap it key = sequence val = list of words
        
        wordMap = defaultdict(list)
        
        for i,e in enumerate(strings):
            
            #calculate sequence
            seq1 = '0'
            seq2 = '0'
            for j in range(1,len(e)):
                
                if e[j] == e[j-1]:
                    seq1 += '0'
                    continue
                #scenario 1 current > past
                if ord(e[j]) > ord(e[j-1]): 
                    num1 = (25 - (ord(e[j]) - ord('a'))) + (ord(e[j-1]) - ord('a') +1)
                    #num2 = ord(e[j]) - ord(e[j-1]) 
                    seq1 += str(num1)
                    #seq2 += str(num2)
                #scenario 2 current < past
                else:
                    #num1 = (25 - ord(e[j-1]) - ord('a')) + ord(e[j])
                    num1 = ord(e[j-1]) - ord(e[j])
                    seq1 += str(num1)
                    #seq2 += str(num2)
                
                
                seq1 += ','
                #num = ord(e[j-1]) - ord(e[j])
                #print(num)
                #seq += str(num)
            
            wordMap[seq1].append(e)
            #wordMap[seq2].append(e)
        
        
        #print(wordMap)
        res = []
        
        for key,val in wordMap.items():
            res.append(val)
        
        return res