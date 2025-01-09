class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        l = len(needle)
        for i, h in enumerate(haystack):
            if h == needle[0]:
                if needle == haystack[i : i + l]:
                    return i
        return -1
