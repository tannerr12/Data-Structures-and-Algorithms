class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.stock = defaultdict(lambda:defaultdict(int))
        self.rentedStatus = defaultdict(lambda:defaultdict(int))
        self.rented = []
        self.nonrented = defaultdict(list)
        for shop,movie,price in entries:
            self.stock[movie][shop] = price
            heappush(self.nonrented[movie], [price, shop])
            
    def search(self, movie: int) -> List[int]:      
        ans = []
        poped = []
        seen = set()
        while self.nonrented[movie] and len(ans) < 5:
            p,s = heappop(self.nonrented[movie])
            
            if s in self.stock[movie] and s not in seen:
                seen.add(s)
                ans.append(s)
                poped.append([p,s])
        
        for p,s in poped:
            heappush(self.nonrented[movie], [p,s])
        
        return ans

    def rent(self, shop: int, movie: int) -> None:
        price = self.stock[movie][shop]
        heappush(self.rented, [price, shop, movie])
        del self.stock[movie][shop]
        self.rentedStatus[movie][shop] = price
        
    def drop(self, shop: int, movie: int) -> None:
        price = self.rentedStatus[movie][shop]
        self.stock[movie][shop] = price
        heappush(self.nonrented[movie], [price, shop])
        del self.rentedStatus[movie][shop]

    def report(self) -> List[List[int]]:
        
        ans = []
        poped = []
        seen = set()
        while self.rented and len(ans) < 5:
            p,s,m = heappop(self.rented)
            
            if s in self.rentedStatus[m] and (s,m) not in seen:
                seen.add((s,m))
                ans.append([s,m])
                poped.append([p,s,m])
        
        for p,s,m in poped:
            heappush(self.rented, [p,s,m])
        
        return ans
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()