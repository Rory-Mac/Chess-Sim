from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        items = {num : i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            if items.get(target - num, None) != None and items[target - num] != i:
                return [i, items[target - num]]
