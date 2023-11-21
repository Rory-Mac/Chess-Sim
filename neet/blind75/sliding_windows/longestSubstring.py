# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s : str) -> int:
        # boundary cases
        if len(s) < 2: 
            return len(s)
        if len(s) == 2: 
            return 2 if s[0] != s[1] else 1
        # initialise pointers
        l = 0
        r = 1
        seen = {}
        seen[s[l]] = 0
        max_count = 0
        char_count = 1
        while r < len(s):
            if s[r] in seen:
                max_count = max(max_count, char_count)
                m = seen[s[r]] + 1
                while l < m:
                    seen.pop(s[l])
                    l += 1
                    char_count -= 1
                seen[s[r]] = r
                char_count += 1
                r += 1
            else:
                seen[s[r]] = r
                r += 1
                char_count += 1
        return max(max_count, char_count)