class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        w1 = Counter(word1)
        w2 = Counter(word2)
        
        if len(w1.keys()) == len(w2.keys()):
            for key,val in w1.items():
                    # add 1 to w2
                    for k,v in w2.items():
                        #uniques
                        if v == 1 and w1[key] == 1 and k not in w1 and key not in w2:
                            return True
                        if v > 1 and w1[key] > 1 and k not in w1 and key not in w2:
                            return True
                        if k in w1 and key in w2:
                            return True

            return False

        if abs(len(w1) - len(w2)) > 2:
            return False
        # word1 and word2 have more than 1 same character (can swap one for a unique (+1,0)
        target = abs(len(w1) - len(w2))
        if len(w1) > len(w2):
            for key,val in w1.items():

                    for k,v in w2.items():

                        if target == 2 and w1[key] == 1 and key not in w2 and k in w1:
                            return True
                        if target == 1:
                            if w1[key] == 1 and key in w2:
                                if v > 1 and key != k:
                                    return True
                            if w1[key] == 1 and key not in w2:
                                if v == 1 and k in w1:
                                    return True
                            if w1[key] > 1 and key not in w2 and k in w1:
                                if v > 1 and key != k:
                                    return True
        if len(w2) > len(w1):                    
            for key,val in w2.items():
                # add 1 to w2


                    for k,v in w1.items():

                        if target == 2 and w2[key] == 1 and key not in w1 and k in w2:
                            return True

                        if target == 1:
                            if w2[key] == 1 and key in w1:
                                if v > 1 and key != k:
                                    return True
                            if w2[key] == 1 and key not in w1:
                                if v == 1 and k in w2:
                                    return True
                            if w2[key] > 1 and key not in w1 and k in w2:
                                if v > 1 and key != k:
                                    return True

        return False         
                
            
            