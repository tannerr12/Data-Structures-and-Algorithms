class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        
        restaurants.sort(key = lambda x: (-x[1], -x[0]))
        
        #print(restaurants)
        
        arr = []
        
        for i in range(len(restaurants)):
            a,b,c,d,e = restaurants[i]
            if veganFriendly == 0 or veganFriendly == c:
                if d <= maxPrice and e <= maxDistance:
                    arr.append(a)
        
        return arr