def counting_sort(items, magnitude):
    item_counts = [0] * 10
    results = [0] * len(items)
    for item in items:
        index = (item // magnitude) % 10
        item_counts[index] += 1
    for i in range(1, 10):
        item_counts[i] += item_counts[i - 1]
    for i in range(1, len(items) + 1):
        count_index = (items[-i] // magnitude) % 10
        results[item_counts[count_index] - 1] = items[-i]
        item_counts[count_index] -= 1
    for i in range(len(items)):
        items[i] = results[i]

def radix_sort(items):
    max_item = max(items)
    magnitude = 1
    while max_item // magnitude > 0:
        counting_sort(items, magnitude)
        magnitude *= 10

if __name__ == "__main__":
    items = [121, 432, 402, 0, 10, 564, 23, 1, 40, 45, 788, 20, 140]
    radix_sort(items)
    assert items == [0, 1, 10, 20, 23, 40, 45, 121, 140, 402, 432, 564, 788]