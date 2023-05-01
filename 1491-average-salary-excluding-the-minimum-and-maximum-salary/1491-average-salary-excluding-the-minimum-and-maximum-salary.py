class Solution:
    def average(self, salary: List[int]) -> float:
        mn = min(salary)
        mx = max(salary)
        
        s = sum(salary)
        
        return (s - mn - mx) / (len(salary) - 2)