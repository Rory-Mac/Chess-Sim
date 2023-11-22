def prefix_sum(items):
    for i in range(1, len(items)):
        items[i] += items[i - 1]

def count_sort(items):
    max_item = max(items)
    item_count = [0 for _ in range(max_item + 1)]
    for item in items:
        item_count[item] += 1
    prefix_sum(item_count)
    result = [0 for _ in range(len(items))]
    for i in range(1, len(items) + 1):
        item = items[-i]
        index = item_count[item] - 1
        item_count[item] -= 1
        result[index] = item
    return result

if __name__ == "__main__":
    nums = [2,5,3,0,2,3,0,3] 
    assert count_sort(nums) == [0,0,2,2,3,3,3,5]