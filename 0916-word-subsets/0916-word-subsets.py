class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        w2Global = defaultdict(int)
        for word in words2:
            count = defaultdict(int)
            for char in word:
                count[char] +=1
            
            for key, val in count.items():
                w2Global[key] = max(w2Global[key], val)
        
        res = []
        for word in words1:
            w1Map = Counter(word)
            valid = True
            for key,val in w2Global.items():
                if w1Map[key] < val:
                    valid = False
                    break
            
            if valid:
                res.append(word)
        
        return res
        