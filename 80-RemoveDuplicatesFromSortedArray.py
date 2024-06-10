class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        remaining=len(nums)
        i=1
        while i <= remaining -2:
            if nums[i] == nums[i-1] and nums[i-1] == nums[i+1]:
                nums.pop(i)
                remaining -= 1
            else:
                i += 1
        return remaining

        