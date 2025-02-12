class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for el in nums[1:]:
            if el > nums[i]:
                i += 1
                nums[i] = el
        for j in range(i+1, len(nums)):
            nums[j] = "_"
        print(nums)
        return i+1