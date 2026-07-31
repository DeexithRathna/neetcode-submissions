class Solution:
    cache = {}
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            type(self).cache[n] = n
            return type(self).cache[n]
        else:
            if type(self).cache.get(n):
                return type(self).cache[n]
            else:
                type(self).cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
                return type(self).cache[n]
        