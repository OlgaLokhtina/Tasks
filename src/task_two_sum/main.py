class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        rez = []
        for elem in nums:
            for ind in range(nums.index(elem) + 1, len(nums)):
                if elem + nums[ind] == target:
                    rez = [nums.index(elem), ind]
                    break
            if rez:
                break
        return rez
