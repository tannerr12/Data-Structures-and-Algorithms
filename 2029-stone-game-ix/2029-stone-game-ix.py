class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        def check(start):
            mod = defaultdict(int)

            for i in range(len(stones)):
                mod[stones[i] % 3] += 1

            count = 0
            turn = 0

            if mod[start]:
                mod[start] -= 1
                count = start
            else:
                return False

            turn = 1
            if mod[0] % 2:
                turn = 0


            while mod[1] or mod[2]:
                if count == 2 and mod[2]:
                    mod[2] -= 1
                    count = 1
                    turn = not turn
                elif count == 1 and mod[1]:
                    mod[1] -= 1
                    count = 2
                    turn = not turn
                else:
                    return turn
            
        if check(1) or check(2):
            return True
        return False