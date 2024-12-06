#https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/

#https://www.youtube.com/watch?v=jUM_Dpt6yu0&ab_channel=mCoding

#CHECK THIS !!!
def selection_sort(arr: set) -> list: 
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


def lumberSelection(capacity:int , prices:list[int]):
    length = [1,2,4,6,8,10,12]
    
    # create 2D matrix for table
    #table = [[0 for _ in range(capacity + 1)] for _ in range(len(prices) + 1)]
    i:int=0
    j:int=0
    table = [[0 for i in range(capacity + 1)] for j in range(len(prices) + 1)]

    # Calculate maximum profit for each 
    # item index and knapsack weight.
    #start at biggest and move backwards
    for i in range(len(prices) - 1, -1, -1):
        for j in range(1, capacity + 1):

            take = 0
            if j - length[i] >= 0:
                take = prices[i] + table[i][j - length[i]]
            noTake = table[i + 1][j]

            #fine max of take/no take, set that to place in table
            if take>noTake:
                table[i][j] =take
            else:
                table[i][j] =noTake

            #table[i][j] = max(take, noTake)
            #print(table[i][j])

    #table in final row will have max price
    return table[0][capacity]



def calcPermutations(val:int) -> None:
    bills = [100, 50, 20, 10, 5, 2, 1] 
    all_combinations :set[int] = set()  # Use a set to avoid duplicates
    stack = [(val, [])]  # Initialize stack with the target bill and an empty combination

    while stack:
        current_bill, current_combination = stack.pop()
        print("curlen",current_bill)
        print("cur_comb", current_combination)

        if current_bill == 0:
            # Add the combination as a tuple to the set
            all_combinations.add(tuple(selection_sort(current_combination)))
            continue

        for bill in bills:
            if bill <= current_bill:
                # Create a new combination with the current bill included
                new_combination :list[int]= current_combination + [bill]
                print("new combination", new_combination)
                stack.append((current_bill - bill, new_combination))
                print("stack", stack)

    for combination in selection_sort(all_combinations):
         print(list(combination))



def getNumberOfWays(change_amount:int, bill_list:list[int]) -> int:
    all_combinations :set[int] = set()  # Use a set to avoid duplicates
    stack = [(change_amount, [])]  # Initialize stack with the target bill and an empty combination
    numberWays :int=0
    #same as permuations, but COUNT it at end <3
    while stack:
        current_bill, current_combination = stack.pop()
        if current_bill == 0:
            # Add the combination as a tuple to the set
            all_combinations.add(tuple(selection_sort(current_combination)))
            continue
        for bill in bill_list:
            if bill <= current_bill:
                # Create a new combination with the current bill included
                new_combination :list[int]= current_combination + [bill]
                stack.append((current_bill - bill, new_combination))
    for combination in selection_sort(all_combinations):
        numberWays+=1
    return numberWays



# Main function to execute the combination finding
def main():
    prices :list[int] = [0.25, 1.45, 3.58, 4.40,5.18, 6.58, 8.28]
    wt = [1, 2,4,6,8,10,12]
    bills = [100, 50, 20, 10, 5, 2, 1]
    target_length = 9  # 12 feet
    all_combinations = calcPermutations(target_length)


    capacity :int = 12
    #print(lumberSelection(capacity, prices))
    #print(calcPermutations(4))
    #print(getNumberOfWays(6, bills))

if __name__ == "__main__":
    main()

