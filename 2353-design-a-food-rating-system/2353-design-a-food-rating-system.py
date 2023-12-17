class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.score = {}
        self.group = defaultdict(list)
        self.type = {}
        for i in range(len(foods)):
            heappush(self.group[cuisines[i]], [-ratings[i], foods[i]])
            self.score[foods[i]] = -ratings[i]
            self.type[foods[i]] = cuisines[i]
    def changeRating(self, food: str, newRating: int) -> None:
        self.score[food] = -newRating
        heappush(self.group[self.type[food]], [-newRating, food])

    def highestRated(self, cuisine: str) -> str:
     
        while self.group[cuisine] and self.group[cuisine][0][0] != self.score[self.group[cuisine][0][1]]:
            heappop(self.group[cuisine])
        
        return self.group[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)