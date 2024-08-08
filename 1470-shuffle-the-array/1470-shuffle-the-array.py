class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = [0] *(2*n)
        k = 0
        for i in range(0, n):
            arr[k] = nums[i]
            arr[k+1] = nums[i+n]
            k+=2
        return arr
            
            