class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr =[[] for i in range(len(nums) +1)]
        
        
        for num in count.keys():
            arr[count[num]].append(num)
        
        res = []
        for i in range(len(arr) -1, -1, -1):
            
            for val in arr[i]:
                res.append(val)
                if len(res) == k:
                    return res