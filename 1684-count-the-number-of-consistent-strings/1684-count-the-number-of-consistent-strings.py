class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        a = set(allowed)
        res = 0
        for w in words:
            found = False
            for j in w:
                if j not in a:
                    found = True
            if not found:
                res +=1
        

        return res