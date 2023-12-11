class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = defaultdict(int)
        most = 0
        cnt = 0
        for i in range(200):
            
            idx = random.randint(0,len(arr)-1)
            c[arr[idx]] +=1
            if c[arr[idx]] > cnt:
                most = arr[idx]
                cnt = c[arr[idx]]
        
        return most