class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        
        
        
        #how many permutations start with 1
        #9! would be 1/9 of the options is our answer greater than this?
        
        ans = []
        has = set([i for i in range(1, n + 1)])
        pos = n
        while len(ans) != n:
            total = factorial(pos)
            i = 1
            for val in sorted(has,reverse=True):
                if k > (total // pos) * (len(has) -i):
                    k -= (total // pos) * (len(has) -i)
                    ans.append(str(val))
                    break
                i += 1
            has.remove(int(ans[-1]))
            pos -= 1
        
        #print(ans)
        
        return ''.join(ans)
            