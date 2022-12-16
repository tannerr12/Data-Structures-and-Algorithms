
from sortedcontainers import SortedSet
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        os = SortedSet()
        od = defaultdict(dict)
        
        
        for name,table,food in orders:
            
            os.add(food)
            if food not in od[table]:
                od[table][food] = 0
            od[table][food] += 1
            
        
       
        res = []
        
        header = ['Table'] + list(os)
        
        #print(header)
        res.append(header)
        
        for i in range(1,501):
        
            if str(i) in od:
                row = []
                row.append(str(i))
                for v in os:
                    if v in od[str(i)]:
                        row.append(str(od[str(i)][v]))
                    else:
                        row.append('0')
                
                res.append(row)
        
        
        return res
                    
                    