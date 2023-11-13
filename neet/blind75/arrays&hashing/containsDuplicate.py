class ContainsDuplicateI(object):
    # with hashing
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
    
    # sort the input array and determine if adjacent elements are equal
    def containsDuplicateAlternative(self, nums):
        deep_copy = [num for num in nums]
        deep_copy.sort()
        for i in range(1, len(deep_copy)):
            if deep_copy[i] == deep_copy[i - 1]:
                return True
        return False

    # brute force approach
    def containsDuplicateNaive(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue
                if nums[i] == nums[j]: return True
        return False
    
# Given an integer array nums and an integer k, return true if there are two distinct indices
# i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
class ContainsDuplicateII(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        items = []
        item_indices = {}
        for num in nums:
            items.append(num)
            new_item_index = len(items)
            if item_indices.get(num, None) == None:
                item_indices[num] = [new_item_index]
            else:
                for item_index in item_indices[num]:
                    if abs(item_index - new_item_index) <= k:
                        return True    
                item_indices[num].append(new_item_index)
        return False
