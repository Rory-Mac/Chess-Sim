class ProductofArrayExceptSelf(object):
    # O(n) time complexity + O(n) space complexity
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix_product = [0] * len(nums)
        prefix_product[0] = nums[0]
        for i in range(1,len(nums)):
            prefix_product[i] = nums[i] * prefix_product[i - 1]
        suffix_product = [0] * len(nums)
        suffix_product[-1] = nums[-1]
        for i in range(2, len(nums) + 1):
            suffix_product[-i] = nums[-i] * suffix_product[-i + 1]
        answer = [0] * len(nums)
        for i in range(len(nums)):
            if i - 1 < 0:
                answer[i] = suffix_product[i + 1]
            elif i + 1 == len(nums):
                answer[i] = prefix_product[i - 1]
            else:
                answer[i] = prefix_product[i - 1] * suffix_product[i + 1]
        return answer
    
    # O(n) time complexity + O(1) space complexity (excluding result array)
    def productExceptSelfAlternative(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(nums)
        answer[-1] = nums[-1]
        for i in range(2, len(nums) + 1):
            answer[-i] = nums[-i] * answer[-i + 1]
        answer[0] = answer[1]
        prefix_product = nums[0]
        for i in range(1, len(nums) - 1):
            answer[i] = prefix_product * answer[i + 1]
            prefix_product *= nums[i]
        answer[-1] = prefix_product
        return answer