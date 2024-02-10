"""

"""
import itertools as it
import math
from collections import Counter
from typing import Self
import numpy as np

from permutils import PermutationUtils


class Permutation:
    def __init__(self, data: list[int]):
        assert len(set(data)) == len(data), 'All elements of permutation must be unique.'
        assert max(data) == len(data), 'The permutation S_N must contain all elements from 1 to N.'
        self.__data = data
        self.__cycleform = self._cycleform()
        self.order = self._order()
        self.cycle_structure = self._cycle_structure()

    @property
    def cycleform(self):
        return self.__cycleform

    @cycleform.setter
    def cycleform(self, value):
        raise ValueError('Nonsettable variable!')

    def __repr__(self):
        return '{' + f'{", ".join(map(str, self.__data))}' + '}' + f' {self.cycle_structure}-cycle'

    def __len__(self):
        return len(self.__data)

    def __getitem__(self, item):
        return self.__data[item]

    def __mul__(self, other: Self) -> Self:
        return Permutation([other[x - 1] for x in self])

    def __invert__(self):
        result = [0] * len(self)
        for i in range(len(self)):
            result[self[i] - 1] = i + 1
        return Permutation(result)

    def __pow__(self, power: int, modulo=None):
        power %= self.order
        if power == 0:
            return Permutation.neutral(len(self))
        result = self
        for _ in range(abs(power) - 1):
            result *= self
        return result

    def __eq__(self, other):
        return self.__data == other.__data

    def matrix(self) -> np.array:
        length = len(self)
        A = np.zeros((length, length))
        for i in range(length):
            A[i][self[i] - 1] = 1
        return A

    def _cycleform(self) -> list[list[int]]:
        """
        reduced: remove 1-len cycles, e.g. (1)(2)(4, 3) => (4, 3)
        :return:
        """
        result = []
        proccessed = []

        def findNext(point):
            maybeNext = self[point - 1]
            if maybeNext == start:
                return
            result[-1].append(maybeNext)
            proccessed.append(maybeNext)
            return maybeNext

        for i in range(len(self)):
            start = i + 1
            if start in proccessed:
                continue
            result.append([start])
            proccessed.append(start)
            next_ = start
            while True:
                next_ = findNext(next_)
                if next_ is None:
                    break

        return result

    def _order(self) -> int:
        return math.lcm(*[len(cycle) for cycle in self.cycleform])

    def _cycle_structure(self) -> tuple[int, ...]:
        return tuple(sorted([len(cycle) for cycle in self.cycleform if len(cycle) > 1]))

    def altisEven(self) -> bool:
        """
        This method is slower then isEven(). Just for academical aims.
        :return:
        """
        return np.linalg.det(self.matrix()) == 1

    def isEven(self) -> bool:
        return len([len(cycle) for cycle in self.cycleform if len(cycle) % 2 == 0]) % 2 == 0

    def isConjugateWith(self, other):
        return self.cycle_structure == other.cycle_structure

    def isDerangement(self):
        """
        Does the permutation leave fixed elements. {x: P(x) = x}
        Can be implemented via checking length of fixedElements.
        :return:
        """
        return sum(self.cycle_structure) == len(self)

    def fixedElements(self):
        return [x for x in self.__data if self.__data.index(x) + 1 == x]

    def describe(self):
        return f'{self}, {self.cycle_structure}-cycle'

    def passport(self):
        """
        Such structure {x1 : k1, x2: k2, . . . }, that xi - length of cycle i, and ki - count of cycles with length i.
        :return:
        """
        return Counter([len(cycle) for cycle in self.cycleform])

    def getCommutativeStructures(self) -> list[tuple]:
        """
        :return: List of cyclic structures that commute with a given permutation.
        """
        results = []
        for p in Permutation.generateAll(len(self)):
            if p == Permutation.neutral(len(self)):
                continue
            if p.cycle_structure in results:
                continue
            if self * p == p * self:
                results.append(p.cycle_structure)
        return results

    def getStabilizingStructures(self, leftMult=False) -> list[tuple]:
        """
        :return: List of cyclic structures that stabilize (not changing cycle structure) a given permutation.
        """
        results = []
        for p in Permutation.generateAll(len(self)):
            if p == Permutation.neutral(len(self)):
                continue
            if p.cycle_structure in results:
                continue
            answer = p * self if leftMult else self * p
            if answer.cycle_structure == self.cycle_structure:
                results.append(p.cycle_structure)
        return results

    def getRootStructures(self, degree: int = 2) -> list[tuple]:
        """
        :param degree:
        :return:
        :return: List of cyclic structures that can obtain by n-degree root extraction of given permutation.
        """
        results = []
        for p in Permutation.generateAll(len(self)):
            if p.cycle_structure in results:
                continue
            if p ** degree == self:
                results.append(p.cycle_structure)
        return results

    @staticmethod
    def generateExampleOfCertainStruct(struct: list[int], cardinality: int):
        """
        :param cardinality:
        :param struct:
        :return:
        """
        if not struct:
            return Permutation.neutral(cardinality)
        result = []
        ommited_ones = cardinality - sum(struct)
        assert ommited_ones >= 0, 'Invalid argument: struct or cardinality.'
        start = 1
        for x in struct:
            result.extend([j for j in range(start + 1, start + x)])
            result.append(start)
            start += x
        for _ in range(ommited_ones):
            result.append(start)
            start += 1
        return Permutation(result)

    @staticmethod
    def createEmbassyOfGroup(cardinality: int):
        """
        We create a representative from each cyclic structure. Increases the speed of calculations.
        :param cardinality:
        :return:
        """
        return [Permutation.generateExampleOfCertainStruct(struct, cardinality) for struct in PermutationUtils.cycle_patitions(cardinality)]

    @staticmethod
    def neutral(cardinality: int):
        return Permutation(list(range(1, cardinality + 1)))

    @staticmethod
    def generateAll(cardinality: int):
        return (Permutation(list(comb)) for comb in it.permutations(range(1, cardinality + 1)))





