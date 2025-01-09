
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        m_set = set(magazine)
        occ = {l: 0 for l in m_set}
        for l in magazine:
            occ[l] += 1
        for l in ransomNote:
            if not l in m_set or occ[l] < 1:
                return False
            else:
                occ[l] -= 1
        return True
