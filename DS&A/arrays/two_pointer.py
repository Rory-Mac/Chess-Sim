# given an array A with n integers, find if there exists a pair of elements a, b that belong to A with sum equal to x
def pair_exists_with_sum(A, x):
    # deep copy
    items = []
    for item in A:
        items.append(item)
        items.sort()
    # two pointer technique
    hi = len(items) - 1
    lo = 0
    while True:
        if lo == hi:
            return False
        candidate_sum = items[lo] + items[hi]
        if candidate_sum == x:
            return True
        elif candidate_sum > x:
            hi -= 1
        elif candidate_sum < x:
            lo += 1

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9]
    assert pair_exists_with_sum(nums, 3)
    assert not pair_exists_with_sum(nums, 2)
    assert pair_exists_with_sum(nums, 11)
    assert not pair_exists_with_sum(nums, 27)
    nums = [123,314,514,645,346,245,32,1229,1]
    assert pair_exists_with_sum(nums, 591)
    assert not pair_exists_with_sum(nums, 592)
    assert pair_exists_with_sum(nums, 1230)
    assert not pair_exists_with_sum(nums, 1229)