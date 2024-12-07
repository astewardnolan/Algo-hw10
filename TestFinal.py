import final

def test_selection_sort():
    print("Testing selection_sort:")
    print(final.selection_sort({3, 1, 4, 2}))  # Expected: [1, 2, 3, 4]
    print(final.selection_sort({}))  # Expected: []
    print(final.selection_sort({1}))  # Expected: [1]
    print(final.selection_sort({5, 3, 2, 1, 4}))  # Expected: [1, 2, 3, 4, 5]
    print(final.selection_sort({-1, 0, 1}))  # Expected: [-1, 0, 1]
    print()

def test_lumber_selection():
    print("Testing lumberSelection:")
    prices = [0.25, 1.45, 3.58, 4.40, 5.18, 6.58, 8.28]
    print(final.lumberSelection(3, prices))  # Expected: 1.70
    print(final.lumberSelection(0, prices))  # Expected: 0
    print(final.lumberSelection(1, prices))  # Expected: 0.25
    print(final.lumberSelection(10, prices))  # Expected: 8.61
    print()

def test_find_permutations_iteratively():
    print("Testing find_permutations_iteratively:")
    print(final.find_permutations_iteratively(3))  # Expected: {(2, 1), (1, 1, 1)}
    print(final.find_permutations_iteratively(0))  # Expected: set()
    print(final.find_permutations_iteratively(1))  # Expected: {(1,)}
    print(final.find_permutations_iteratively(2))  # Expected: {(2,), (1, 1)}
    print()

def test_calc_permutations():
    print("Testing calcPermutations:")
    print("Combinations for 5:")
    final.calcPermutations(5)  # Expected: Various combinations that sum to 5
    print("Combinations for 0:")
    final.calcPermutations(0)  # Expected: []
    print("Combinations for 1:")
    final.calcPermutations(1)  # Expected: [1]
    print()

def test_get_number_of_ways():
    print("Testing getNumberOfWays:")
    bills = [1, 2, 5]
    print(final.getNumberOfWays(6, bills))  # Expected: 5
    print(final.getNumberOfWays(0, bills))  # Expected: 1 (one way to make zero)
    print(final.getNumberOfWays(1, bills))  # Expected: 1
    print(final.getNumberOfWays(2, bills))  # Expected: 2
    print(final.getNumberOfWays(3, bills))  # Expected: 3
    print()

def main():
    test_selection_sort()
    test_lumber_selection()
    test_find_permutations_iteratively()
    test_calc_permutations()
    test_get_number_of_ways()

if __name__ == "__main__":
    main()
