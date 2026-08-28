class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        min_k = 1
        while min_k <= max_k:
            mid = ( min_k + max_k ) // 2
            time = 0
            for pile in piles:
                time = time + math.ceil(pile/mid)
            if time <= h:
                # Search in left half to find min
                res = mid
                max_k = mid - 1
            else:
                min_k = mid + 1
        return res


        