class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        remaining=len(nums)
        i=0
        while i < remaining:
            if nums[i] == val:
                nums[i] = nums[-1]  
                nums.pop()  
                remaining -= 1 
            else:
                i=i+1
        return remaining
        