class Node:
    
    def __init__(self, url):
        
        self.url = url
        self.back = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.node = Node(homepage)

    def visit(self, url: str) -> None:
        self.node.next = Node(url)
        n = self.node.next
        n.back = self.node
        self.node = self.node.next
        self.node.url = url
        #self.node.next = None

    def back(self, steps: int) -> str:
        
        while steps and self.node.back:
            self.node = self.node.back
            steps -=1
        
        return self.node.url

    def forward(self, steps: int) -> str:
        
        while steps and self.node.next:
            self.node = self.node.next
            steps -=1
        
        return self.node.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)