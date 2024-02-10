from graphs import drawRootGraph, drawCommutativeGraph, drawStabilizingGraph
from permutation import Permutation
from permutils import PermutationUtils

if __name__ == '__main__':
    p = Permutation([4, 5, 3, 1, 2])
    print(p)
    print(~p)  # Invert
    print(p.order)
    print(p.cycleform)
    print(p.cycle_structure)
    print(p.isDerangement())
    print(p.isEven())
    print(p ** 51, p ** -64)  # Quick power, due to using order
    print(p.matrix())

    # Example of (2, 3, 7) cycle in S15 group.
    print(Permutation.generateExampleOfCertainStruct([2, 3, 7], 15))
    # Find count of (2, 2, 2)-cycles in S8 group
    print(PermutationUtils.countOfCertainCycleform([2, 2, 2], cardinality=8))

    # Find count of permutation, whuch commuting with (3, 3)-cycles in S10
    print(PermutationUtils.countOfCommutingWithCycleform([3, 3], cardinality=10))

    drawRootGraph(6)

    drawCommutativeGraph(5)

    drawStabilizingGraph(5)

