class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #Knuth Morris Pratt KMP 
        
        #https://www.youtube.com/watch?v=JoF0Z7nVSrA
        
        #first we will setup our prefix - postfix for the needle where anytime the characters match we increase both pointers by 1 and since our lps pointer is the number of matched characters
        #we make our arrays position = the new lps position
        #if we dont have a match we shift our lps pointer backwards in the array to where we had a match so if we hit a 2 we go to poition 2 since we will know that there were 2 matches at that point
        lps = [0] * len(needle)
        plps = 0
        i = 1
        
        while i < len(needle):
            
            if needle[plps] == needle[i]:
                
                lps[i] = plps + 1
                plps +=1 
                i+=1
            elif plps == 0:
                lps[i] = 0
                i+=1
            else:
                
                plps = lps[plps-1]

        #haystack
        i = 0
        #needle
        j = 0
        #this part will go over haystack and if we have a match we can shift both pointers
        #same idea here when we dont have a match get the last match length based on the value of the array and set our lps pointer to that
        #for both we have a base case where if we reach the start of the array theres nothing left the check for matching so we might as well start over and increment through haystack
        while i < len(haystack):
            
            if needle[j] == haystack[i]:
                i+=1
                j+=1
            
            elif j == 0:
                i+=1
            
            else:
                j = lps[j-1]
            
            #our j will ahead of our return target so we just return the haystack position - length of needle 
            if j >= len(needle):
                return i - len(needle)
        
        return -1
                