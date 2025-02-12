class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        string = min(strs)
        prefix = ""
        a = ""
        for sym in string:
            a = a + sym
            for s in strs:
                if a not in s:
                    return prefix
            prefix = a
        return prefix

