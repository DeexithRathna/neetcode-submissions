import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap_list = [( point[0]*point[0] + point[1]*point[1], index, point[0] , point[1]) for index, point in enumerate(points)]
        print(heap_list)
        heapq.heapify(heap_list)
        print(heap_list)
        res = heapq.nsmallest(k, heap_list)
        closest_points = []
        for item in res:
            closest_points.append([item[2], item[3]])
        return closest_points
