class Solution:
    def convertArray(self, nums: List[int]) -> int:


        def min_cost(nums):
            min_heap = []
            cost = 0
            for num in nums:
                if min_heap and num > min_heap[0]:
                    cost += num - heapq.heappushpop(min_heap, num)
                heapq.heappush(min_heap, num)
            return cost
        return min(min_cost(nums), min_cost([-num for num in nums]))