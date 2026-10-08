class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_heap = []
        answer = []

        for coords in points:
            d = coords[0]**2 + coords[1]**2

            heapq.heappush(points_heap, (d, coords[0], coords[1]))
        
        for i in range(k):
            d, x, y = heapq.heappop(points_heap)

            answer.append([x, y])
        
        return answer
        