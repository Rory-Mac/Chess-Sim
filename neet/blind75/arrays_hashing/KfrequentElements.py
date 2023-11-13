# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_frequencies = {}
        for num in nums:
            candidate = num_frequencies.get(num, None)
            if candidate == None:
                num_frequencies[num] = 1
            else:
                num_frequencies[num] += 1