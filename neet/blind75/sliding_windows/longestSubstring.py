# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    # create left and right pointer, l and r
    # create hash map 'seen'
    # create char_count and max_count
    # while r < len(s):
    #   if current char s[r] is not in seen
    #       add s[r]:r key-value to seen
    #       increment char count
    #       increment r
    #   else:
    #       update max_count
    #       next = s[r] + 1
    #       while l < next:
    #           remove s[l] from hash map
    #           increment l
    #           decrement char count
    #       re-add s[r] to the hash map
    # update the max count
    # return max count
    def lengthOfLongestSubstring(self, s : str) -> int:
        # boundary cases
        if len(s) < 2:
            return len(s)
        # algorithm
        l = 0
        r = 1
        seen = {}
        seen[s[l]] = 0
        max_count = 0
        char_count = 1
        while r < len(s):
            if s[r] not in seen:
                seen[s[r]] = r
                char_count += 1
                r += 1
            else:
                max_count = max(max_count, char_count)
                new_l = seen[s[r]] + 1
                while l < new_l:
                    seen.pop(s[l])
                    l += 1
                    char_count -= 1
                seen[s[r]] = r
                r += 1
                char_count += 1
        return max(max_count, char_count)
    
    # simplify code
    def lengthOfLongestSubstringAlt(self, s : str) -> int:
        l = 0
        seen = set()
        max_count = 0
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                max_count = max(max_count, r - l + 1)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
        return max_count