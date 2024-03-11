class Solution:
    def customSortString(self, order: str, s: str) -> str:

        alph = [100 for i in range(26)]
  
        for i,x in enumerate(order):

            val = ord(x) - ord('a')

            alph[val] = i 


        #print(alph)


        def mergeSort(arr):
            
            if len(arr) <= 1:
                return arr
            left = mergeSort(arr[:len(arr)//2])
            right = mergeSort(arr[len(arr)//2:])


            l,r = 0,0
            res = []
            while l < len(left) and r < len(right):
                alphaL = ord(left[l]) - ord('a')
                alphaR = ord(right[r]) - ord('a')
                if alph[alphaL] < alph[alphaR]:
                    res.append(left[l])
                    l+=1
                else:
                    res.append(right[r])
                    r +=1
            


            res.extend(left[l:])
            res.extend(right[r:])

            return res

        #res = mergeSort(s)


        #return ''.join(res)

        h = Counter(s)
        r = ''
        for x in order:

            if x in h and h[x] > 0: 
                r += (x * h[x])
                del h[x]
        

        for x,y in h.items():
            r += (x * y)

        return r


