class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ls = set()
        for i,e in enumerate(emails):
            mid = e.find('@')
            
            left = e[:mid]
            right = e[mid+1:]
            #remove after +
            if '+' in left:
                plus = left.find('+')
                left = left[:plus]
            #remove . from left
            left = left.replace('.', '')
            
            email = left + '@' + right
            
            ls.add(email)
            
        
     
        return len(ls)
            
            