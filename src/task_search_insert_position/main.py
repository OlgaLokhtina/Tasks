class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        try:
            v: int = nums.index(target)
        except ValueError:
            for j in range(len(nums)):
                if target < nums[j]:
                    v: int = j
                    break
                v: int = j + 1
        return v
