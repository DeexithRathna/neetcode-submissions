class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        total = 0
        for i in range(len(operations)):
            if operations[i] == 'C':
                total = total - scores.pop()
            elif operations[i] == 'D':
                scores.append(2*scores[-1])
                total = total + scores[-1]
            elif operations[i] == '+':
                scores.append(scores[-1] + scores[-2])
                total = total + scores[-1]
            else:
                scores.append(int(operations[i]))
                total = total + scores[-1]
            # print(total)
            # print(scores)
        return total