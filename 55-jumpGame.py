class Solution:
    def canJump(self, nums: List[int]) -> int:
        n = len(nums)
        farthest=0
        if n == 1: 
            return True
        for i in range(n-1):
            if i > farthest:
                break
            farthest = max(farthest, i + nums[i])
            if farthest >= n-1:
                return True
        
        return False
