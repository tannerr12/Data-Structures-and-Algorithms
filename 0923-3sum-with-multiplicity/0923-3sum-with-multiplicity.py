class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        c = Counter(arr)
        MOD = 10 ** 9 + 7
        ls = list(c)
        ls.sort()
        
        #print(c)
        #print(ls)
        res = 0
        for i in range(len(ls)):
            for j in range(i, len(ls)):
         
                need = target - ls[i] - ls[j]
                if need < ls[j]:
                    continue
                totalNeed = c[need]

                if ls[i] == need:
                    totalNeed -=1
                if ls[j] == need:
                    totalNeed -=1

                totalI = c[ls[i]]
                totalJ = c[ls[j]]

                if ls[i] == ls[j]:
                    totalJ -= 1

                if totalI > 0 and totalJ > 0 and totalNeed > 0: 
                    if ls[i] == ls[j] == need:
                        res += factorial(totalI) // (factorial(3) * factorial(totalI - 3))

                    elif ls[j] == need:
                        res += ((totalNeed * (totalNeed + 1)) // 2) * totalI
                    elif ls[i] == ls[j]:
                        res += totalNeed * ((totalJ * (totalJ + 1)) // 2)
                    else:
                        res += max(0, totalI * totalJ * totalNeed)

                    res %= MOD

        return res
                
                
                
                
                
                