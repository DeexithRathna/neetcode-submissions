class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map = {}
        for key, value in zip(s,t):
            if key not in hash_map:
                if value not in hash_map.values():
                    hash_map[key] = value
                else:
                    return False
            else:
                if hash_map[key] != value:
                    return False
        return True
        