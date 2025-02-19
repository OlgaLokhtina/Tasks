from main import Solution


def test_removeElement():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    expectedNums = [0, 0, 1, 3, 4]
    a = Solution()
    k = a.removeElement(nums, val)
    assert k == len(expectedNums)
    nums[0:k] = sorted(nums[0:k])
    for i in range(k):
        assert nums[i] == expectedNums[i]
