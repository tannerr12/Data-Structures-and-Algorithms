class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        time = 0
        cost = 0
        for i in range(len(customers)):
            
            arr,t = customers[i]
            if time < arr:
                time = arr
            tcost = max(0, time - arr) + t
            time += t
            cost += tcost
            
        
        
        return cost / len(customers)
            
            
            