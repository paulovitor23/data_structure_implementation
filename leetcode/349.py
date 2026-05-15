from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        result = []
        for v in nums2:
            if v in seen:
                result.append(v)
                seen.remove(v)
        return result
