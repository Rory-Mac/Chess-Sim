# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and
# nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

class ThreeSum(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        solutions = []
        for skip, num in enumerate(nums):
            target_sum = -num
            i = 0 if skip != 0 else 1
            j = len(nums) - 1 if skip != len(nums) - 1 else len(nums) - 2
            while i < j:
                if i == skip:
                    i += 1
                if j == skip:
                    j -= 1
                candidate_sum = nums[i] + nums[j]
                if candidate_sum == target_sum:
                    solutions.append([num, nums[i], nums[j]])
                    i += 1
                    j -= 1
                elif candidate_sum < target_sum:
                    i += 1
                elif candidate_sum > target_sum:
                    j -= 1
        return solutions