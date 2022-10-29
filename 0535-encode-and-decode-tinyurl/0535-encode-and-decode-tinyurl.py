class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        prefix = 'http://tinyurl.com/'
        self.database = {}
        self.id = 0
        self.database[self.id] = longUrl
        return prefix + str(self.id)
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        ts = ''
        i = len(shortUrl) -1
        while shortUrl[i] != '/':
            ts = ts + shortUrl[i]
            
            i-=1
            
        
        return self.database[int(ts)]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))