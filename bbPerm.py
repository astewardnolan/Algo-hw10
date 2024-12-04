# Define the available lengths and their prices
lengths = [12, 10, 8, 6, 4, 2, 1]  # lengths in feet
prices = {
    1: 0.25,
    2: 1.45,
    4: 3.58,
    6: 4.40,
    8: 5.18,
    10: 6.58,
    12: 8.28
}

# Function to find all unique combinations of cuts iteratively
def find_combinations_iteratively(target_length):
    all_combinations = set()  # Use a set to avoid duplicates
    stack = [(target_length, [])]  # Initialize stack with the target length and an empty combination

    while stack:
        current_length, current_combination = stack.pop()
        print("curlen",current_length)
        print("cur_comb", current_combination)

        if current_length == 0:
            # Add the combination as a tuple to the set
            all_combinations.add(tuple(sorted(current_combination)))
            continue

        for length in lengths:
            print("l",length)
            if length <= current_length:
                print("l", length)
                # Create a new combination with the current length included
                new_combination = current_combination + [length]
                print("new combination", new_combination)
                stack.append((current_length - length, new_combination))
                print("stack", stack)

    return all_combinations

# Main function to execute the combination finding
def main():
    target_length = 9  # 12 feet
    all_combinations = find_combinations_iteratively(target_length)

    # Print all unique combinations
    print("All possible unique combinations to cut a 12' board:")
    for combination in sorted(all_combinations):
        print(list(combination))

# Execute the main function
if __name__ == "__main__":
    main()