from main import Solution


def test_longestPref():
    s = Solution()
    assert s.longestCommonPrefix(["flowers", "fly", "flow"]) == "fl", "Should be 'fl'"
    assert s.longestCommonPrefix(["flowers", "opfly", "flow"]) == "fl", "Should be ''"
