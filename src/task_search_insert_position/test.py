from main import Solution


def test_searchInsert():
    a = Solution()
    nums = [1, 2, 4, 7]
    target = 3
    expected = 2
    assert a.searchInsert(nums, target) == expected, f"Should be {expected}"