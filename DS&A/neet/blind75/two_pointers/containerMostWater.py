# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            new_area = min(height[i], height[j]) * abs(i - j)
            max_area = max(max_area, new_area)
            if height[i] < height[j]:
                i += 1
            elif height[i] >= height[j]:
                j -= 1
        return max_area