class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] *(2*len(nums))
        k = 0
        for j in range(len(nums)):
            ans[k] = nums[j]
            ans[k+len(nums)] = nums[j]
            k += 1
            
        return ans
            