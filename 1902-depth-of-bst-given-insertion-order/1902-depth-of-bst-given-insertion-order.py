#from sortedcontainers import SortedList
class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
        #contruct tree and keep track of max depth
        """
        res = 0
        
        def bs(l,r,tar):
            
            while l <= r:
                
                mid = (l + r) // 2
                
                if order[mid] > tar and order[mid-1] < tar:
                    return mid
                elif order[mid] > tar:
                    r = mid - 1
                
                else:
                    l = mid + 1
            
            return l
            
        
        def dfs(l,r,depth):
            nonlocal res
            if l <= r:
                res = max(res, depth)
            if l >= r:
                return
            #binary search for mid
            mid = bs(l+1, r, order[l])
                    
            dfs(l +1, mid-1, depth + 1)
            dfs(mid, r, depth + 1)
        
        dfs(0,len(order) -1,1)
        
        return res
        """
        """
        sl = SortedList()
        dic = defaultdict(int)
        
        res = 0
        
        for val in order:
            
            idx = bisect_left(sl, val)
            total = 0
            if idx != 0:
                total = dic[sl[idx-1]]
            
            if idx != len(sl):
                total = max(total,dic[sl[idx]])
                
            
            sl.add(val)
            
            dic[val] = total + 1
            res = max(res,dic[val])  
        
        return res
        """
        
        n = len(order)
        parents = [0] * (n + 1)
        insert_orders = [0] * (n+1)
        
        for i,v in enumerate(order,1):
            insert_orders[v] = i
        
        stack = []
        
        for node, insert_order in enumerate(insert_orders):
            while stack and insert_orders[stack[-1]] > insert_order:
                prevNode = stack.pop()
                if insert_orders[parents[prevNode]] < insert_order:
                    parents[prevNode] = node
            
            if stack:
                parents[node] = stack[-1]
            stack.append(node)
            
        depths = [0] * (n+1)
        for num in order:
            depths[num] = depths[parents[num]] + 1
        
        return max(depths)
        
        
        