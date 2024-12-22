SYM_MAP = {
    "I": {
        "val": 1,
        "prev": None },
    "V": {
        "val": 5,
        "prev": "I" },
    "X": {
        "val": 10,
        "prev": "I" },
    "L": {
        "val": 50,
        "prev": "X" },
    "C": {
        "val": 100,
        "prev": "X" },
    "D": {
        "val": 500,
        "prev": "C" },
    "M": {
        "val": 1000,
        "prev": "C" },
    }

class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        summ, last_val = 0, 0
        for sym in s[::-1]:
            val = SYM_MAP[sym]["val"]
            if val < last_val:
                summ -= val
            else:
                summ += val
            last_val = val

        return summ