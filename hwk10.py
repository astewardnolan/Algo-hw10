# unbounded knapsack problem using tabulation
#https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/




 

def permutations_iterative(iterable, r=None):
    items = tuple(iterable)
    n = len(items)
    r = n if r is None else r
    if r>n:
        return
    indices= list(range(n))

    for _ in _permuations_iterative_no_stack(indices, r):
        yield tuple(items[indices[i]] for i in range(r))
    

def _permuations_iterative_no_stack(items, r0):
    n = len(items)
    yield
    for i, ticks in countdown(n, r0):
        tick = ticks[i]
        if tick ==0:
            items.append(items.pop(i))
        else:
            j=n-tick
            items[i], items[j] = items[j], items[i]
            yield

def countdown(n,r):
    ticks = list(range(n,n-r, -1))
    while True:
        for i in reversed(range(r)):
            ticks[i] -=1
            yield i , ticks
            if ticks[i] == 0 :
                ticks[i]= n-i
            else:
                break

        else:
            return



def lumberSelection(capacity:int , prices:list[int]):
    wt = [1,2,4,6,8,10,12]
    
    # 2D matrix for tabulation.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(prices) + 1)]

    # Calculate maximum profit for each 
    # item index and knapsack weight.
    for i in range(len(prices) - 1, -1, -1):
        for j in range(1, capacity + 1):

            take = 0
            if j - wt[i] >= 0:
                take = prices[i] + dp[i][j - wt[i]]
            noTake = dp[i + 1][j]

            dp[i][j] = max(take, noTake)
            #print(dp[i][j])

    return dp[0][capacity]






if __name__ == "__main__":
    prices :list[int] = [0.25, 1.45, 3.58, 4.40,5.18, 6.58, 8.28]
    wt = [1, 2,4,6,8,10,12]
    capacity :int = 3
    print(lumberSelection(capacity, prices))



    #perms= list(permutations_iterative(wt,12))
    #print(perms)