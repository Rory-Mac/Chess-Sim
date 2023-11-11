def binary_search(items, lo, hi, item):
    if lo > hi: return False
    mid = (hi + lo) // 2
    if items[mid] == item: return True
    if items[mid] < item:
        return binary_search(items, mid + 1, hi, item)
    elif items[mid] > item:
        return binary_search(items, lo, mid - 1, item)

if __name__ == "__main__":
    items = [-2048,-76,-14,-1,1,7,24,61,64,79,95,323,885,9917]
    inital_lo = 0
    initial_hi = len(items) - 1
    assert binary_search(items, inital_lo, initial_hi, 1)
    assert binary_search(items, inital_lo, initial_hi, 7)
    assert not binary_search(items, inital_lo, initial_hi, 9)
    assert binary_search(items, inital_lo, initial_hi, -76)
    assert binary_search(items, inital_lo, initial_hi, -2048)
    assert not binary_search(items, inital_lo, initial_hi, -2049)