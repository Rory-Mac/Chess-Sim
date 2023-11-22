from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while numbers[i] + numbers[j] != target:
            s = numbers[i] + numbers[j]
            if s < target:
                i += 1
            else:
                j -= 1
        return [i + 1, j + 1]