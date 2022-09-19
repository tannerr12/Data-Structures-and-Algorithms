class Trie:
    def __init__(self):
        self.char = ''
        self.childWords = []
        self.children = {}
        self.end = False
        


class Solution:
    
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        #add all of the words and if word contains prefix add it to result o(N) or o{n log n}
        products.sort()
        self.t = Trie()
        
        
        def add(word):
            temp = self.t
            
            for c in word:
                
                if c in temp.children:
                    temp.childWords.append(word)
                    temp = temp.children[c]
                    
                else:
                    y = Trie()
                    y.char = c
                    temp.children[c] = y
                    temp.childWords.append(word)
                    temp = temp.children[c]
            
            temp.end = True
            temp.childWords.append(word)
            
            
        
        
        for word in products:
            add(word)
            
        res = []
        #print(self.t.children)
        
        def search(word):
            done = False
            
            for c in word:
                
            #    print(self.t.children)
            #    print(self.t.childWords)
                if c in self.t.children and not done:
                    self.t = self.t.children[c]
                  
                    res.append(self.t.childWords[:3])
                else:
                    res.append([])
                    done = True
            
        
        
        search(searchWord)
        
        return res