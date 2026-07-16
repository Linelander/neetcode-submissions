class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge and find median? I don't really see the issue
        nums3 = []

        while nums1 or nums2:
            one = nums1[0] if nums1 else float('inf')
            two = nums2[0] if nums2 else float('inf')
            if one < two:
                nums3.append(nums1.pop(0))
            else:
                nums3.append(nums2.pop(0))

        if len(nums3) % 2 == 1:
            return nums3[len(nums3) // 2]
        return (nums3[(len(nums3) // 2) - 1] + nums3[(len(nums3) // 2)]) / 2