class Solution:

    delimiter = "#EOW"

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result = result + word + self.delimiter
        return result

    def decode(self, s: str) -> List[str]:
       return s.split(self.delimiter)[:-1]
