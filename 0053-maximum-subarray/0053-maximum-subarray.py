class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        max_so_far = nums[0]
        max_end_here = 0
        for n in nums:
            max_end_here = max_end_here + n
            if max_so_far < max_end_here:
                max_so_far = max_end_here
            if max_end_here < 0:
                max_end_here = 0
            
        return max_so_far
        
#         maxsum = nums[0]
#         currsum = 0
#         for n in nums:
#             currsum = max(currsum, 0)
#             currsum += n
#             maxsum = max(currsum, maxsum)
        
#         return maxsum
        # max_so_far = float('=inf')
        
            