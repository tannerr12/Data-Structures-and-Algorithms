class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        
        numset = set(['0','1','2','3','4','5','6','7','8','9'])
        res = ''
        
        arr = sentence.split(' ')
        discount = 100 - discount
        if discount > 0:
            discount = discount / 100
        for i in range(len(arr)):
            
            word = arr[i]
            
            if word[0] == '$':
                #scan the word
                num = ''
                decCount = 0
                notNum = False
                for j in range(1,len(word)):
                    if word[j] in numset:
                        num += word[j]
                    elif word[j] == '.':
                        decCount +=1
                        num += word[j]
                    else:
                        notNum = True
                        break
                
                if notNum == False and decCount <= 1 and len(word) > 1:
                    new = float(num) * discount
                    new = '{0:.2f}'.format(new)
                    res += ' $' + str(new)
                else:
                    res += ' ' + word
            else:
                res += ' ' + word
    
        
        return res[1:]
            
            
            
            
            