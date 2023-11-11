def prefix_sum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
        
def count_sort(nums):
    max_num = max(nums)
    count = [0 for _ in range(max_num + 1)]
    for num in nums:
        count[num] += 1
    prefix_sum(count)
    result = [0 for _ in nums]
    for i in range(1, len(nums) + 1):
        num = nums[-i]
        index = count[num] - 1
        count[num] -= 1
        result[index] = num
    return result

if __name__ == "__main__":
    nums = [2,5,3,0,2,3,0,3] 
    assert count_sort(nums) == [0,0,2,2,3,3,3,5]