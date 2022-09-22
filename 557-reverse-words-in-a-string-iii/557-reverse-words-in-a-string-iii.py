class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        arr = s.split(' ')

        
        
        for j in range(len(arr)):
            word = arr[j]
            l,r = 0, len(word) -1
            temps = ''
            for i in range(len(word) -1,-1,-1):
                temps += word[i]
            
            
            word = temps
            
            arr[j] = word
             

        

        
        return ' '.join(arr)