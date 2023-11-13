class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        items = {}
        for num in nums:
            if items.get(num, None) != None:
                return True
            items[num] = num
        return False
