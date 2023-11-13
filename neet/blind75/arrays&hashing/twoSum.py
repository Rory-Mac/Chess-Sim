#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.
class TwoSum(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        items = {}
        for i, num in enumerate(nums):
            items[num] = i
        for i, num in enumerate(nums):
            candidate = items.get(target - num, None)
            if candidate and candidate != i:
                return [i, candidate]
