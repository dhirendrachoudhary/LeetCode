class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        interSection = set()
        for n1 in nums1:
            if n1 in nums2:
                interSection.add(n1)
    
        return interSection
        