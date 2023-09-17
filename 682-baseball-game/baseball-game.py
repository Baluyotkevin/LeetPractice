class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            if operations[i] == '+':
                record.append(int(record[-1]) + int(record[-2]))
            elif operations[i] == 'D':
                record.append(int(record[-1]) * 2)
            elif operations[i] == 'C':
                record.remove(record[-1])
            else:
                record.append(int(operations[i]))
        total = 0
        for i in range(len(record)):
            total += record[i]
        return total