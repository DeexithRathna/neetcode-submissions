class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) >= 1 :
            max_len = len(set(s))
            for window_size in range(max_len, 1, -1):
                offset = 0
                while offset + window_size <= len(s):

                    word = s[offset:offset+window_size]
                    if len(word) == len(set(word)):
                        return len(word)
                    else:
                        offset += 1
            return 1
        else:
            return 0
            
        