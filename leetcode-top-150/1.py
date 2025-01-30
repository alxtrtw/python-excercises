class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        diff = None
        for i, num in enumerate(nums):
            diff = -(num - target)
            rest = nums[i + 1:]
            if diff in rest:
                return i, rest.index(diff) + i + 1
