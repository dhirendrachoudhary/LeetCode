class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        interSection = []
        for n1 in nums1:
            if n1 in nums2 and n1 not in interSection:
                interSection.append(n1)
    
        return interSection
        