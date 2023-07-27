class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        arr1 = []
        arr2 = []
        
        for val in s1:
            arr1.append(val)
        for val in s2:
            arr2.append(val)
        
        arr1.sort(reverse=True)
        arr2.sort(reverse=True)
        
        #print(arr1)
        #print(arr2)
        break1 = True
        break2 = True
        for i in range(len(s1)):
            
            if arr1[i] < arr2[i]:
                break1 = False
            if arr2[i] < arr1[i]:
                break2 = False
        
        return break1 or break2
        