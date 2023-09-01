class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:

        heapq.heapify(blocks)
        while len(blocks) > 1:
            block_1 = heapq.heappop(blocks)
            block_2 = heapq.heappop(blocks)
            new_block = block_2 + split
            heapq.heappush(blocks, new_block)
        return blocks[0]
        '''
        blocks.sort(reverse=True)
        
        @lru_cache(maxsize=100000)
        def dfs(i,w):
            
            if i >= len(blocks):
                return 0
            
            if w >= len(blocks) - i:
                return blocks[i]
            
            if w <= 0:
                return float('inf')
            
            res = float('inf')
            #assign worker to block
            res = min(res, max(blocks[i], dfs(i+1, w-1)))
            
            #split all workers
            res = min(res, dfs(i, w * 2) + split)
            
            
            return res
        
        return dfs(0, 1)
        '''