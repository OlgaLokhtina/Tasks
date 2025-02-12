class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = nums.count(val)
        for i in range(n):
            nums.remove(val)
            nums.append("_")
        print(nums)
        return len(nums) - n