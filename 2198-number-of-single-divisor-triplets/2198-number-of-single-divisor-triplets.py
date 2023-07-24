class Solution:
    def singleDivisorTriplet(self, nums: List[int]) -> int:
        #max sum is 300 -> a + b + c
        #cant have duplicates
        c = Counter(nums)
        ls = list(c)
        res = 0

            
        for i in range(len(ls)):
            for j in range(i, len(ls)):
                for k in range(j, len(ls)):
                    # skip if not enough instances for a valid triplet
                    if (ls[i] == ls[j] and c[ls[i]] < 2) or (ls[i] == ls[k] and c[ls[i]] < 2) or (ls[j] == ls[k] and c[ls[j]] < 2):
                        continue

                    val = ls[i] + ls[j] + ls[k]
                    if (val % ls[i] == 0 and val % ls[j] != 0 and val % ls[k] != 0) or (val % ls[i] != 0 and val % ls[j] == 0 and val % ls[k] != 0) or (val % ls[i] != 0 and val % ls[j] != 0 and val % ls[k] == 0):
                        if ls[j] == ls[k]:
                            res += 3 * (c[ls[j]]) * (c[ls[j]]-1) * c[ls[i]]
                        elif ls[i] == ls[j]:
                            res += 3 * (c[ls[i]]) * (c[ls[i]]-1) * c[ls[k]]
                        else:
                            res += 6 * (c[ls[i]] * c[ls[j]] * c[ls[k]]) 

        return res
                    
                    
            
                
        
            