# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        
        N = reader.length()
        q1 = reader.query(0,1,2,3)
        same = 1
        diff = 0
        diffIndex = None
        for i in range(4, N):
            q2 = reader.query(0,1,2,i)
            
            if q1 == q2:
                same +=1
            else:
                diff +=1
                if diffIndex is None:
                    diffIndex = i
        #0 and 3
        q1 = reader.query(1,2,3,4)
        q2 = reader.query(0,1,2,4)

        if q1== q2:
            same +=1
        else:
            diff +=1
            if diffIndex is None:
                diffIndex = 0

        #1 and 3
        q1 = reader.query(0,2,3,4)
        q2 = reader.query(0,1,2,4)


        if q1 == q2:
            same +=1
        else:    
            diff  +=1
            if diffIndex is None:
                diffIndex = 2
        #1 and 3
        q1 = reader.query(0,1,3,4)
        q2 = reader.query(0,1,2,4)


        if q1 == q2:
            same +=1
        else:    
            diff  +=1
            if diffIndex is None:
                diffIndex = 3

        if same > diff:
            return 3
        elif same < diff:
            return diffIndex
        else:
            return -1