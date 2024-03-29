class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        # Custom sorting function
        def custom_sort(x):
            return (x[0] < x[1], -x[0] if x[0] < x[1] else x[1])

        # Sorting transactions using the custom sort function
        transactions.sort(key=custom_sort)

        
        #print(transactions)
        
        #9 - 2 = 7 + 1 = 8
        #8 - 4 = 4 + 2 = 6
        #6 - 5 = 1 + 0 = 1
        
        
        #9 - 4 = 5 + 2 = 7
        #7 - 2 = 5 + 1 = 6
        #6 - 5 = 1
        
        #9 - 5 = 4
        #4 - 4 = 0 + 2 = 2
        #2 - 2 = 0 + 1 = 1
        
        
        #  0 -> -7 -> -8
        # -5 -> -9 -> -9
        
        # -1 -5 -9
        # -2 -6 -9
        
        # -5 -6 -8
        # -5 -7 -10
        mn = 0
        cur = 0
        for x,y in transactions:
            cur -= x
            mn = min(mn,cur)
            cur += y
        
        return mn * -1