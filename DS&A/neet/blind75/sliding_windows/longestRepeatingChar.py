# Longest Repeating Character Replacement
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase 
# English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        counts = collections.Counter()
        largest_count = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            largest_count = max(largest_count, counts[s[r]])
            if (r - l + 1) - largest_count <= k:
                max_len = max(max_len, r - l + 1)
            else:
                counts[s[l]] -= 1
                l += 1
        return max_len

