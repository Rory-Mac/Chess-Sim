# return the maximum sum of k consecutive elements in the given array
def max_consecutive_sum(items, k):
    lo = 0
    hi = 0
    max_sum = 0
    current_sum = 0
    while hi < k:
        current_sum += items[hi]
        hi += 1
    max_sum = current_sum
    while hi < len(items):
        current_sum = current_sum + items[hi] - items[lo]
        if current_sum > max_sum: 
            max_sum = current_sum
        lo += 1
        hi += 1
    return max_sum

if __name__ == "__main__":
    items = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    assert max_consecutive_sum(items, 4) == 39
    assert max_consecutive_sum(items, 5) == 47