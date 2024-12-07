# Name:  - Ashby Steward-Nolan  and Ashley Jagai
# Peers:  - N/A
# References:  
#https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/
#https://www.youtube.com/watch?v=jUM_Dpt6yu0&ab_channel=mCoding



from collections import deque

# Function to perform selection sort on a set
def selection_sort(arr: set) -> list:
    """
    Sorts a set of numbers into a list in ascending order using the selection sort algorithm.

    Parameters:
    arr (set): The input set to be sorted.

    Returns:
    list: A sorted list of numbers in ascending order.

    Example:
    >>> selection_sort({3, 1, 4, 2})
    [1, 2, 3, 4]
    """
    # Convert the set to a list so we can work with indices
    arr_list = list(arr)
    
    # Loop through the entire list (which is now a list derived from the set)
    for i in range(len(arr_list)):
        # Find the index of the minimum element in the unsorted part of the list
        min_index = i
        for j in range(i + 1, len(arr_list)):
            if arr_list[j] < arr_list[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr_list[i], arr_list[min_index] = arr_list[min_index], arr_list[i]
    
    # Return the sorted list
    return arr_list


# Function to solve the lumber selection problem using dynamic programming (Unbounded Knapsack)
def lumberSelection(capacity: int, prices: list[int]) -> int:
    """
    ***ASSUMES cuts of wood (length list) will ALWAYS be the same !!***

    Solves the lumber selection problem using dynamic programming to maximize profit
    based on a given capacity and price list for various lengths of boards.

    Parameters:
    capacity (int): The total length of the lumber available to cut.
    prices (list[int]): A list of prices for various lengths of boards.

    Returns:
    int: The maximum price that can be obtained by cutting the lumber.

    Example:
    >>> prices = [0.25, 1.45, 3.58, 4.40, 5.18, 6.58, 8.28]
    >>> lumberSelection(3, prices)
    1.70
    """
    length = [1, 2, 4, 6, 8, 10, 12]
    
    # Create 2D matrix for table
    table = [[0 for _ in range(capacity + 1)] for _ in range(len(prices) + 1)]

    # Calculate maximum profit for each item index and knapsack weight
    for i in range(len(prices) - 1, -1, -1):
        for j in range(1, capacity + 1):
            take = 0
            if j - length[i] >= 0:
                take = prices[i] + table[i][j - length[i]]
            noTake = table[i + 1][j]

            # Take the maximum of "take" or "noTake"
            if take > noTake:
                table[i][j] = take
            else:
                table[i][j] = noTake
    # Return the max price from the first row of the table
    return table[0][capacity]


# Function to find all unique combinations of cuts using an iterative approach
def find_permutations_iteratively(target_length: int) -> set:
    """
    Finds all unique combinations of cuts that sum up to a target length using an iterative approach.

    Parameters:
    target_length (int): The total length of the board to be cut.

    Returns:
    set: A set of unique combinations of lengths that sum up to the target length.

    Example:
    >>> find_permutations_iteratively(3)
    {(2, 1), (1, 1, 1)}
    """
    lengths = [12, 10, 8, 6, 4, 2, 1]
    all_combinations = set()  # Use a set to avoid duplicates
    stack = [(target_length, [])]  # Initialize stack with the target length and an empty combination

    while stack:
        current_length, current_combination = stack.pop()

        if current_length == 0:
            # Add the combination as a tuple to the set
            all_combinations.add(tuple(selection_sort(current_combination)))
            continue

        for length in lengths:
            if length <= current_length:
                # Create a new combination with the current length included
                new_combination = current_combination + [length]
                stack.append((current_length - length, new_combination))

    return all_combinations


# Function to calculate all unique combinations of bills to make up a specific value
def calcPermutations(val: int) -> None:
    """
    Calculates all unique combinations of bills that sum up to a given value using a stack-based approach.

    Parameters:
    val (int): The target value to be formed using bills.

    Returns:
    None: Prints all combinations that sum to the target value.

    Example:
    >>> calcPermutations(5)
    [5]
    [2, 2, 1]
    [2, 1, 1, 1]
    [1, 1, 1, 1, 1]
    """
    bills = [100, 50, 20, 10, 5, 2, 1]
    all_combinations: set[int] = set()  # Use a set to avoid duplicates
    stack = deque()
    stack = [(val, [])]  # Initialize stack with the target bill and an empty combination

    while stack:
        current_bill, current_combination = stack.pop()
        if current_bill == 0:
            # Add the combination as a tuple to the set
            all_combinations.add(tuple(selection_sort(current_combination)))
            continue

        for bill in bills:
            if bill <= current_bill:
                # Create a new combination with the current bill included
                new_combination: list[int] = current_combination + [bill]
                stack.append((current_bill - bill, new_combination))

    for combination in selection_sort(all_combinations):
        print(list(combination))


# Function to calculate the number of unique ways to make a specific amount of change
def getNumberOfWays(change_amount: int, bill_list: list[int]) -> int:
    """
    Calculates the number of unique ways to make a specific amount of change using given bill denominations.

    Parameters:
    change_amount (int): The target amount of change to be made.
    bill_list (list[int]): The list of available bill denominations.

    Returns:
    int: The total number of unique ways to make the change.

    Example:
    >>> getNumberOfWays(6, [1, 2, 5])
    5
    """
    all_combinations: set[int] = set()  # Use a set to avoid duplicates
    stack = [(change_amount, [])]  # Initialize stack with the target bill and an empty combination
    numberWays: int = 0

    # Same as permutations, but count it at the end
    while stack:
        current_bill, current_combination = stack.pop()
        if current_bill == 0:
            # Add the combination as a tuple to the set
            all_combinations.add(tuple(selection_sort(current_combination)))
            continue
        for bill in bill_list:
            if bill <= current_bill:
                # Create a new combination with the current bill included
                new_combination: list[int] = current_combination + [bill]
                stack.append((current_bill - bill, new_combination))
    
    # Count the number of unique combinations
    for combination in selection_sort(all_combinations):
        numberWays += 1
    return numberWays


# Main function to execute the combination finding and lumber selection
def main():

    prices: list[int] = [0.25, 1.45, 3.58, 4.40, 5.18, 6.58, 8.28]
    target_length = 3  # Target lumber length

    # Find all combinations of cuts for a given target length
    all_combinations = find_permutations_iteratively(target_length)

    for combination in all_combinations:
        print(combination)

    # Calculate all permutations of bills for a given amount
    #print(calcPermutations(12))

    # Calculate number of ways to make change for a given amount
    bills = [100, 50, 20, 10, 5, 2, 1]
    #print(getNumberOfWays(6, bills))
    print(lumberSelection(3, prices))


if __name__ == "__main__":
    main()
