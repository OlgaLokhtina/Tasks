class Solution:
    def romanToInt(self, s: str) -> int:
        l = len(s)
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = map[s[l-1]]
        for i in range(l-1, 0, -1):
            if map[s[i]] <= map[s[i - 1]]:
                result += map[s[i - 1]]
            else:
                result -= map[s[i - 1]]
        return result



