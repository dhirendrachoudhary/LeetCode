class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = 0
        globalMax = nums[0]
        currMin = 0
        globalMin = 0
        total = 0
        for n in nums:
            currMax = max(currMax+n, n)
            currMin = min(currMin+n, n)
            total += n
            
            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)
            
                
        return max(globalMax, total-globalMin) if globalMax >0 else globalMax
                