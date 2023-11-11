def count_sort(nums):
    count = [0 for _ in nums]
    for num in nums:
        count[num] += 1
    result = []
    for i in range(len(count)):
        for _ in range(count[i]):
            result.append(i)
    return result

if __name__ == "__main__":
    nums = [2,5,3,0,2,3,0,3] 
    assert count_sort(nums) == [0,0,2,2,3,3,3,5]