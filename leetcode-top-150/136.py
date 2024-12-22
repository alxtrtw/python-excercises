class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums2 = []
        for el in nums:
            if el not in nums2:
                nums2.append(el)
            else:
                nums2.remove(el)
        return nums2[0]

class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res