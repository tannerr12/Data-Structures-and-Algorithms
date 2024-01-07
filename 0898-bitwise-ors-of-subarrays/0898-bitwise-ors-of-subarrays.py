class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        
        
        #1, 4, 1, 3
        
        #1,3
        
        #2
        
        # Tabulation is a list of sets, one for each number in A. 
        # Each set, at position i, is initialised to containing the element at A[i]
        tabulation = [set([A[i]]) for i in range(len(A))]
        
        # And now we need to go through, updating the sets based on the previous set.
        for i in range(1, len(A)):
            for previous_result in tabulation[i - 1]: 
                tabulation[i].add(A[i] | previous_result)  
        
        # Return the number of unique numbers in the tabulation list.
        return len(set.union(*tabulation)) if len(A) > 0 else 0