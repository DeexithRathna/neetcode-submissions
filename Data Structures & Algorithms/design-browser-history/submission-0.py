class Website():
    def __init__(self, url, prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next
       
class BrowserHistory:

    def __init__(self, homepage: str):
        self.website = Website(homepage)
        

    def visit(self, url: str) -> None:
        website = Website(url)
        self.website.next = website
        website.prev = self.website
        self.website = website

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.website.prev:
                self.website = self.website.prev
            else:
                break
        return self.website.url      

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.website.next:
                self.website = self.website.next
            else:
                break
        return self.website.url