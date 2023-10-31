# return deep copy of a provided list after sorting 
def copy_and_sort(A):
    nums = []
    for elem in A:
        nums.append(elem)
    nums.sort()
    return nums

# given an array A with n integers, find if there exists a pair of elements a, b that belong to A with sum equal to x
def sum_pair_exists(A, x) -> bool:
    nums = copy_and_sort(A)
    lo = 0
    hi = len(nums) - 1
    while (True):
        if lo == hi: 
            return False
        candidate_sum = nums[lo] + nums[hi] 
        if candidate_sum == x:
            return True
        elif candidate_sum > x:
            hi -= 1
        elif candidate_sum < x:
            lo += 1

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9]
    assert sum_pair_exists(nums, 3)
    assert not sum_pair_exists(nums, 2)
    assert sum_pair_exists(nums, 11)
    assert not sum_pair_exists(nums, 27)
    nums = [123,314,514,645,346,245,32,1229,1]
    assert sum_pair_exists(nums, 591)
    assert not sum_pair_exists(nums, 592)
    assert sum_pair_exists(nums, 1230)
    assert not sum_pair_exists(nums, 1229)