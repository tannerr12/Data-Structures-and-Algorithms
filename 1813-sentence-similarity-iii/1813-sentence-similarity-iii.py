class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        s1 = sentence1.split(' ')
        s2 = sentence2.split(' ')
        
        #print(s1)
        #print(s2)
        
        def find(s1,s2):
            
            p1,p2 = 0, 0
            skip = False
            gap = 0
            gapCheck = False
            while p1 < len(s1) and p2 < len(s2):

                if s1[p1] == s2[p2]:
                    gapCheck = False
                    p2 += 1
                else:
                    if gapCheck == False:
                        gapCheck = True
                        gap += 1
                    skip = True

                p1 += 1

        
            return gap <= 1 and (p1 == len(s1) and p2 == len(s2)) or (p2 == len(s2) and not skip)
        
        
        res = find(s1,s2) or find(s2,s1) or find(s1[::-1], s2[::-1]) or find(s2[::-1],s1[::-1])
        
        return res