import math
from collections import Counter
from typing import Literal


class PermutationUtils:
    @staticmethod
    def _computeProduct(cycleform: list[int], cardinality: int, degree: Literal[1, -1]):
        assert all(elem > 0 for elem in cycleform), 'All elements must be positive.'
        numOfOmitted_1 = cardinality - sum(cycleform)
        assert numOfOmitted_1 >= 0, 'Invalid cycleform, no respect to cardinality.'
        passport = Counter(cycleform)
        passport[1] += numOfOmitted_1
        result = 1
        for i in passport:
            result *= i ** passport[i] * math.factorial(passport[i])
        return result ** degree

    @staticmethod
    def countOfCertainCycleform(cycleform: list[int], cardinality: int) -> int:
        return int(PermutationUtils._computeProduct(cycleform, cardinality, -1) * math.factorial(cardinality))

    @staticmethod
    def countOfCommutingWithCycleform(cycleform: list[int], cardinality: int) -> int:
        return int(PermutationUtils._computeProduct(cycleform, cardinality, 1))

    @staticmethod
    def _partition(n):
        if n == 0:
            yield []
            return
        for p in PermutationUtils._partition(n - 1):
            p.append(1)
            yield p
            p.pop()
            if p and (len(p) < 2 or p[-2] > p[-1]):
                p[-1] += 1
                yield p

    @staticmethod
    def cycle_patitions(n):
        return [sorted([elem for elem in x if elem != 1]) for x in PermutationUtils._partition(n)]



