# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and
# nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
class ThreeSum(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # a + b + c == 0
        # [-1,2,-3,4,5]
        nums.sort()
        triplets = []
        for x, num in enumerate(nums):
            if x > 0 and num == nums[x - 1]: continue
            i, j = x + 1, len(nums) - 1
            while i < j:
                t = num + nums[i] + nums[j]
                if t < 0:
                    i += 1
                elif t > 0:
                    j -= 1
                else:
                    triplets.append([num, nums[i], nums[j]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
        return triplets