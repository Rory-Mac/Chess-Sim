def radix_sort(nums):
    max_num = max(nums)
    digits = len(str(max_num))
    str_nums = [str(num) for num in nums]
    sorted = []
    for i in range(1, digits):
        counted = [0 for _ in range(len(nums))]
        for num in str_nums:
            if len(num) < i:
                sorted.append(num)




# Expected Behaviour:
# 170 45 75 90 802 24 2 66
# 170 90 802 2 24 45 75 66
# 802 2 24 45 66 170 75 90
# 2 24 45 66 75 90 175 802
if __name__ == "__main__":
    nums = [170,45,75,90,802,24,2,66]
    result = radix_sort(nums)
    assert result == [2,24,45,66,75,90,170,802]