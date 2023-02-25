class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        table = collections.defaultdict(list)
      
        
        def charCount(s):
            arr = [0] *26
            for char in s:
                arr[ord(char) - ord('a')] +=1
            
            
            return ','.join(map(str,arr))
        
        for i in range(len(strs)):
            
            joined = charCount(strs[i])
            
            table[joined].append(strs[i])

            
        return table.values()
            