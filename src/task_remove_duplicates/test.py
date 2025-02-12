from main import Solution


def test_removeDuplicates():
    a = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    expectednums = [0,1,2,3,4]
    k = a.removeDuplicates(nums)
    assert k == len(expectednums)
    for i in range(0, k):
        assert nums[i] == expectednums[i]



