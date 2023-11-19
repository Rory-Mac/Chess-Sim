from typing import List

class Solution:
    # [0,0,0,1,1,2,3,4,4,5,5,6,6,7,7,18,18,18]
    # [18,18,18,7,7,6,6,5,5,4,4,3,2,1,1,0,0,0]
    # hash map mapping nums to counts {}
    # [5,4,3,2,1]
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        num_counts = {}
        for num in nums:
            if num_counts.get(num, None) != None:
                num_counts[num] += 1
            else:
                num_counts[num] = 1
        current_num = None
        total_ops = 0
        previous_ops = 0
        for num in nums:
            if num == current_num: continue
            current_num = num
            total_ops += previous_ops
            previous_ops += num_counts[num]
        return total_ops