class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        
        arr = []
        
        for i,n in enumerate(nums):
            
            arr.append([n,i])
        
        arr.sort()
        
        #print(arr)
        
        prefix = []
        prefix.append(0)
        #postfix = []
        #postfix.append(0)
        count = defaultdict(int)
        cpast = defaultdict(int)
        for x,y in arr:
            prefix.append(prefix[-1] + y)
            count[x] += 1
        
        #for i in range(len(arr)-1,-1,-1):
        #    x,y = arr[i]
        #    postfix.append(postfix[-1] + y)
        
        print(prefix)
        #print(postfix)
        
        for i, (val, j) in enumerate(arr):
            #print(prefix[i])
            #print(prefix[i - cpast[val]])
            left = prefix[i] - prefix[i - cpast[val]]
            l1v = j * (cpast[val])
            l = abs(l1v - left)
            
            right = prefix[i + count[val]] - prefix[i+1]
            r1v = j * (count[val] -1)
            
            r = abs(r1v - right)
            
            res[j] = l + r
            count[val] -=1
            cpast[val] += 1
            
        return res
            
        