# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
class LongestConsecutiveSequence(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        items = set(nums)
        max_count = 0
        for x in nums:
            if x - 1 not in items:
                y = x + 1
                while y in items:
                    y += 1
                max_count = max(max_count, y - x)
        return max_count