class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        l2 = set(list2)
        wtotal = {}
        for i,w in enumerate(list1):
            if w in list2:
                wtotal[w] = i
        
        
        for i,w in enumerate(list2):
            if w in wtotal:
                wtotal[w] += i
        
        words = []
        mn = float('inf')
        for key,val in wtotal.items():
            if val < mn:
                words = [key]
                mn = val
            elif val == mn:
                words.append(key)
            
        
        
        return words