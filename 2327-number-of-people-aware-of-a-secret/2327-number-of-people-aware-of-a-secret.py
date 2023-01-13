class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        """
        1. 1 - > 3,5
        2. 1 
        3. 1,2 -> 5,7
        4. 1,2,3 -> 6, 8
        5. 2,3,4 -> 7, 9
        6. 2,3,4,5,6 -> 8,10 * 2
        7. 3,4,5,6,7,8 - > 9,11
        """
        #find the range of people using binary search
      
        
        
        people = deque()
        pq2 = deque()
        people.append([1 + delay, 1 + forget,1])
        
        day = 1
        dp = [0] * (n +1)
        running = 1
        pq2L = 0
        while day <= n:
            
            while people and people[0][0] <= day:
                s,e,amount = people.popleft()
                pq2L += amount
                pq2.append([e, amount])
            
            while pq2 and pq2[0][0] <= day:
                e,am = pq2.popleft()
                pq2L -= am
                running -= am
                
            if len(pq2) > 0:
                people.append([day + delay, day + forget, pq2L])
                running += pq2L
            
            dp[day] = running
            day +=1
        
       
            
        return dp[n] % ((10 ** 9) + 7)
        
        