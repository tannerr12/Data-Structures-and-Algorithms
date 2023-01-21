class TextEditor:

    def __init__(self):
        self.text = ''
        self.cursor = 0
    def addText(self, text: str) -> None:
        self.text = self.text[:self.cursor] + text + self.text[self.cursor:]
        self.cursor += len(text)

        
    def deleteText(self, k: int) -> int:

        count = min(self.cursor,k)
        start = max(self.cursor - k,0)

            
        self.text = self.text[:start] + self.text[self.cursor:]
        self.cursor = start

        return count

    def cursorLeft(self, k: int) -> str:
        self.cursor = max(self.cursor - k, 0)
        mnCount = max(0,self.cursor-10)
        return self.text[mnCount:self.cursor]

        

    def cursorRight(self, k: int) -> str:

        self.cursor = min(self.cursor + k, len(self.text))
        mnCount = max(0,self.cursor-10)
        return self.text[mnCount:self.cursor]


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)