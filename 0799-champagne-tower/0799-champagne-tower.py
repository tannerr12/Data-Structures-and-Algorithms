class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        
        glass = defaultdict(int)
        glass[(0,0)] = poured
        level = 0
        while level <= query_row:
            
            for i in range(level + 1):
                if glass[(level,i)] > 1:
                    if (level, i) == (query_row, query_glass):
                        return 1
                    
                    excess = glass[(level, i)] - 1
                    excess /= 2
                    glass[(level + 1, i)] += excess
                    glass[(level + 1, i + 1)] += excess
                    del glass[(level,i)]
                if (level, i) == (query_row, query_glass):
                    return glass[(level, i)]
            level += 1

        print()
        return glass[(query_row, query_glass)]
            
        
        