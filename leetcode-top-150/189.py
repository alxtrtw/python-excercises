class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        modk = k % len(nums)
        nums[:] = nums[-modk:] + nums[:-modk]
