class ValidAnagram(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_char_counts = [0] * 26
        t_char_counts = [0] * 26
        for character in s:
            s_char_counts[ord(character) - ord('a')] += 1
        for character in t:
            t_char_counts[ord(character) - ord('a')] += 1
        for i in range(26):
            if s_char_counts != t_char_counts:
                return False
        return True
