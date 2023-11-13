# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequencies = {}
        for num in nums:
            if frequencies.get(num, None) == None:
                frequencies[num] = 1
            else:
                frequencies[num] += 1
        sorted_frequencies = sorted(frequencies.items(), key=lambda item: item[1], reverse= True)
        return [frequency[0] for frequency in sorted_frequencies[:k]]
