class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] < target:
                return 1
            elif nums[0] == target:
                return 0
            else:
                return 0
        
        for i in range(len(nums)-1):
            if nums[i] < target:
                if nums[i+1] >= target:
                    return i+1
                else:
                    continue
            else:
                return 0
        return len(nums)