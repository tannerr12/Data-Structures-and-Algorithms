class Union:
    n = 0
    def __init__(self,r,c):

        self.count = 0
        self.directions = [[-1,0], [1,0],[0,1], [0,-1]]
        self.m= r
        self.n = c
        self.parent = [-1] * (self.m*self.n)
        self.rank = [0] * (self.m*self.n)

    #scan up the parents to find the top parent
    # also update all children on the way up to point to the top parent
    #compression
    def find(self, position):
        
        if self.parent[position] != position:
            self.parent[position] = self.find(self.parent[position])
        
        return self.parent[position]


    def union(self,id1,id2):
     
        rootIndex1 = self.find(id1)
        rootIndex2 = self.find(id2)

        if rootIndex1 != rootIndex2:
            if self.rank[rootIndex1] > self.rank[rootIndex2]:
                self.parent[rootIndex2] = rootIndex1

            elif self.rank[rootIndex1] < self.rank[rootIndex2]:
                self.parent[rootIndex1] = rootIndex2

            else:
                self.parent[rootIndex2] = rootIndex1
                self.rank[rootIndex1] +=1

            self.count -=1

    def place(self,i,j):
    
        #i,j = postion[0],position[1]

        ids = i * self.n + j
        if self.parent[ids] == -1:
            self.count +=1
            self.parent[ids] = ids

        for x,y in self.directions:
            i2,j2 = i + x, j + y

            if i2 >= 0 and i2 < self.m and j2 < self.n and j2 >= 0 and self.parent[i2 * self.n + j2] != -1:
                self.union(ids, i2*self.n + j2)     
        
        return self.count

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        u = Union(m,n)
        result = []

        for i in range(len(positions)):
            x,y = positions[i]
            result.append(u.place(x,y))

        return result

