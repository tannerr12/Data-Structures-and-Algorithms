class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:

        courses.sort(key = lambda x: (x[1], x[0]))

        score = 0
        heap = []
        res = 0
        for i in range(len(courses)):
            if courses[i][0] + score <= courses[i][1]:
                score += courses[i][0]
                res += 1
                heappush(heap, -courses[i][0])
            else:
                if heap and -heap[0] > courses[i][0] and score + heap[0] <= courses[i][1]:
                    score += heappop(heap)
                    score += courses[i][0]
                    heappush(heap, -courses[i][0])
            
            
        return res
            
            
            
                
            
            