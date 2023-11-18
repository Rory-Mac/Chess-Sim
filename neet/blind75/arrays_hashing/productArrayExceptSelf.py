class ProductofArrayExceptSelf(object):
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