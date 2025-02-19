from main import Solution


def test_twoSum():
    a = Solution()
    assert a.twoSum([2, 7, 11, 15], 18) == [1, 2], "Should be [1, 2]"
