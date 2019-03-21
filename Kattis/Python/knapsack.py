
def knapsack(n,size):
    if n == 0 or size == 0:
        return 0
    else if weight[n] > size:
        return knapsack(n-1,C)
    else:
        return max(knapsack(n-1,C), value[n] + knapsack(n-1,C-weight[n]))