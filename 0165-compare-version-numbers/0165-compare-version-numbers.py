class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1,s2 = 0,0
        while True:
            left1,left2 = 0,0
            
            for i in range(s1,len(version1)):
                s1 = i + 1
                if version1[i] == '.':
                    break
                left1 *= 10
                left1 += int(version1[i])


            for i in range(s2,len(version2)):
                s2 = i + 1
                if version2[i] == '.':
                    break
                left2 *= 10
                left2 += int(version2[i])


            if left2 > left1:
                return -1
            elif left2 < left1:
                return 1
        
            elif s1 == len(version1) and s2 == len(version2):
                return 0
        
        return 0
            
        
        