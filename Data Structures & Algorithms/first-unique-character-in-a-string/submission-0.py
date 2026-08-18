from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for char, count in counter.items():
            if count == 1:
                return s.index(char)
        return -1

        