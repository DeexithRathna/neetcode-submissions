class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) >= 1 :
            char_map = {}
            l = 0
            res = 0
            for r in range(len(s)):
                if s[r] in char_map:
                    l = max(char_map[s[r]]+1, l)
                char_map[s[r]] = r
                res = max(res, r-l+1)
            return res
        else:
            return 0
            
        