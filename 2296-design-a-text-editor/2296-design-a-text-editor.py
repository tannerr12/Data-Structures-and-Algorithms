class TextEditor:

    def __init__(self):
        self.text = ''
        self.cursor = 0
    def addText(self, text: str) -> None:
        self.text = self.text[:self.cursor] + text + self.text[self.cursor:]
        self.cursor += len(text)

        
    def deleteText(self, k: int) -> int:

        count = min(self.cursor,k)
        start = self.cursor - k
        if start < 0:
            self.text = self.text[self.cursor:]
            self.cursor = 0
        else:    
            
            self.text = self.text[:self.cursor-k] + self.text[self.cursor:]
            self.cursor = start

        return count

    def cursorLeft(self, k: int) -> str:

        count = max(self.cursor - k, 0)
        self.cursor = count
        if self.cursor == 0:
            return ""
        mnCount = max(0,self.cursor-10)

        return self.text[mnCount:self.cursor]

        

    def cursorRight(self, k: int) -> str:

        count = min(self.cursor + k, len(self.text))
        self.cursor = count
        if self.cursor == len(self.text):
          
            if len(self.text) >= 10:
                return self.text[len(self.text) -10:]
            else:
                return self.text
        
        mnCount = max(0,self.cursor-10)
    
        return self.text[mnCount:self.cursor]


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)