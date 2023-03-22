# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        #print(startUrl)
        #define hostname and extension
        
        hostname = startUrl[7:]
      
        #ext = ''
        if '/' in hostname:
            div = hostname.find('/')
            hostname = hostname[:div]
           # ext = startUrl[div:]
        
        res = set()
        res.add(startUrl)
        #print(hostname)
        #print(ext)
        seen = set()
        
        def dfs(url):
            nonlocal hostname
            if url in seen:
                return
            
            seen.add(url)
            
            for val in htmlParser.getUrls(url):
                if val not in seen:
                    h = val[7:]
                   
                    if '/' in h:
                        div = h.find('/')
                        h = h[:div]
                    
                    if h == hostname:
                        res.add(val)
                        dfs(val)
                    else:
                        seen.add(val)
        
        dfs(startUrl)
        
        return list(res)
                        
        