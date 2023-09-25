from sortedcontainers import SortedList
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        
        tasks.sort()
        workers.sort()
        

            
        res = 0
        #workerIdx = 0
        
        def isGood(ans):
            
            _tasks = SortedList(tasks[:ans])
            _workers = workers[-ans:]
            remain_pills = pills
            
            for worker in _workers:
                task = _tasks[0]
                if worker >= task:
                    # the worker can finish the min task without pill, just move on
                    _tasks.pop(0)
                elif worker + strength >= task and remain_pills:
                    # the worker cannot finish the min task without pill, but can solve it with pill
                    # remove the max task that the strengthened worker can finish instead
                    remove_task_idx = _tasks.bisect_right(worker + strength)
                    _tasks.pop(remove_task_idx - 1)
                    remain_pills -= 1
                else:
                    return False
            return True
        
            
        
        lo, hi = 0, min(len(workers), len(tasks))
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if isGood(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
        
        #number cant take any with pill - 0 choice
        #number cant take any without pill - 1 choice
        #number can take without pill cant take with - 1 choice
        #number can take without and take with - 2 choices
            
            