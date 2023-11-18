# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
class LongestConsecutiveSequence(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [0,1,2,3,4,5,6,7,8,9]
        # [5,6,7,8,9,0,1,2,3,4]
        
        # add elements to hash map
        # for num in nums:
        #   if num has been searched for, skip
        #   while successor exists
        #       if successor has been searched
        #           replace search item with current num and sum of consecutive chains
        #           if larger then max, update maximum
        #       increment consecutive numbers count
        #       get next successor

        
