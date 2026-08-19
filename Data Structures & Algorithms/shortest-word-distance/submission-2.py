class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_position = -1
        word2_positions = -1
        min_distance = len(wordsDict)
        positions = {}
        for index, word in enumerate(wordsDict):
            if word != word1 and word != word2:
                continue
            if word == word1:
                if word not in positions:
                    positions[word1] = index
                elif word2 not in positions and positions[word1] < index:
                    positions[word1] = index
                elif word1 in positions and word2 in positions and abs(index - positions[word2]) < min_distance:
                    min_distance = abs(index - positions[word2])
                    positions[word1] = index
            elif word == word2:
                if word not in positions:
                    positions[word2] = index
                elif word1 not in positions and positions[word2] < index:
                    positions[word2] = index
                elif word1 in positions and word2 in positions and abs(index - positions[word1]) < min_distance:
                    min_distance = abs(index - positions[word1])
                    positions[word2] = index
            if len(positions) == 2:
                min_distance = abs(positions[word1]-positions[word2])
            if min_distance == 1:
                return min_distance
            
        return min(min_distance, abs(positions[word1]-positions[word2]))