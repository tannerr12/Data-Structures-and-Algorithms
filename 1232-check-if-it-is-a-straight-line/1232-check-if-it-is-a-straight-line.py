class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        v1 = coordinates[0]
        v2 = coordinates[1]

        if v2[0] - v1[0] != 0:  # To avoid division by 0
            slope = (v2[1] - v1[1]) / (v2[0] - v1[0])
        else:
            slope = float('inf')

        for i in range(2, len(coordinates)):
            v1 = coordinates[i-1]
            v2 = coordinates[i]

            if v2[0] - v1[0] != 0:  # To avoid division by 0
                current_slope = (v2[1] - v1[1]) / (v2[0] - v1[0])
            else:
                current_slope = float('inf')

            if current_slope != slope:
                return False
        
        return True
