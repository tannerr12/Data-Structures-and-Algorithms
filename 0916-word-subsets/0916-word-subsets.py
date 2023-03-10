class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        #first we want to group together all of the words2 words by taking the max character counts from each
        w2Global = defaultdict(int)
        for word in words2:
            count = defaultdict(int)
            for char in word:
                count[char] +=1
            
            for key, val in count.items():
                w2Global[key] = max(w2Global[key], val)
        
        #now we loop through and check if the current words counts are always greater or equal if not we dont add it to our result
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
        