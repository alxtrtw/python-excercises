from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = -(len(nums) // -2)

        counts = defaultdict(int)

        for n in nums:
            counts[n] = counts[n] + 1
            if counts[n] >= l:
                return n
