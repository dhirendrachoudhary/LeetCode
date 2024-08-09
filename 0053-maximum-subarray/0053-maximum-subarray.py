class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        maxsum = nums[0]
        currsum = 0
        for n in nums:
            currsum = max(currsum, 0)
            currsum += n
            maxsum = max(currsum, maxsum)
        
        return maxsum
            
            