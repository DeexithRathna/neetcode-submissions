class Solution:
    def isHappy(self, n: int) -> bool:
        sumSet = set()
        while True:
            s = sum([int(num)**2 for num in list(str(n))])
            # print('n, s, sumSet = ', n, s, sumSet)
            if s == 1:
                return True
            if s in sumSet:
                return False
            sumSet.add(s)
            n = s