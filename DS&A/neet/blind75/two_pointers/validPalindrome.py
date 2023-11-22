class ValidPalindrome(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [c.lower() for c in s if c.isalnum()]
        i = 0
        for i in range(len(s)//2):
            # ~i equivalent to -i - 1
            if s[i] != s[~i]: return False
        return True


