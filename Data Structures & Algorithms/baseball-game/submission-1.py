class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == '+':
                record.append(record[-1] + record[-2])
            elif op == 'C':
                record = record[:-1]
            elif op == 'D':
                record.append(record[-1] * 2)
            else:
                record.append(int(op))
        total = 0
        for r in record:
            total += r
        return total