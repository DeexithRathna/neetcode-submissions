class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) == 0:
            return [[]]
        elif len(strs) == 1:
            return [strs]
        else:
            result = {}
            for word in strs:
                sorted_word = "".join(sorted(word))
                if sorted_word in result:
                    result[sorted_word].append(word)
                else:
                    result[sorted_word] = [word]

            return list(result.values())
                



        