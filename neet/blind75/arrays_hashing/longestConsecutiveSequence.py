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
        # [100,4,200,1,3,2]
        # [9,8,7,6,5,4,3,2,1]

        items = {num : num for num in nums}
        searched = {}
        max_count = 0
        for num in nums:
            if searched.get(num, None) != None: continue
            successor = num
            consecutive_count = 1
            while True:
                successor += 1
                if items.get(successor, None) == None: break
                consecutive_count += 1
                if searched.get(successor, None) != None:
                    consecutive_count_tail = searched.pop(successor)
                    consecutive_count += consecutive_count_tail - 1
                    break
                else:
                    searched[successor] = successor
            searched[num] = consecutive_count
            if consecutive_count > max_count: max_count = consecutive_count
        return max_count


if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    instance = LongestConsecutiveSequence()
    result = instance.longestConsecutive(nums)
    print(result)