class Solution(object):
    def sort_alphabetically(self, s : str) -> str:
        counts = [0] * 26
        for c in s.lower():
            counts[ord(c) - ord('a')] += 1
        res = ""
        for i in range(26):
            for _ in range(counts[i]):
                res += chr(ord('a') + i)
        return res



if __name__ == "__main__":
    s = "slakdfuicoapdlldzoifu"
    instance = Solution()
    res = instance.sort_alphabetically(s)
    print(res)
    assert res == "aacdddffiikllloopsuuz"
