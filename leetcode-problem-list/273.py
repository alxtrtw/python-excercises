th_names = ["", " Thousand ", " Million ", " Billion ", " Trillion ", " Quadrillion ", 
            " Quintillion ", " Sextillion ", " Septillion ", " Octillion ", " Nonillion ",
            " Decillion ", " Undecillion "]
# th_vals = [10**e for e in [3 * n for n in range(1, 12)]]
th_vals = range(13)
th_map = dict(zip(th_vals, th_names))

tens_names = ["Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]
tens_vals = list(map(str, [n for n in range(2, 10)]))
tens_map = dict(zip(tens_vals, tens_names))

teens_names = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", 
               "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
teens_vals = list(map(str, ([10+n for n in range(10)])))
teens_map = dict(zip(teens_vals, teens_names))

uni_names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
uni_vals = list(map(str, range(10)))
uni_map = dict(zip(uni_vals, uni_names))

class Solution(object):

    def subdivide_num(self, num):
        
        snum = str(num)
        groups = []
        while snum != "":
            left, right = snum[:-3], snum[-3:]
            groups.append(right)
            snum = left

        return groups[::-1]
    
    def translate_group(self, group):

        result = ""

        if len(group) == 3:
            if group[0] != '0':
                result += uni_map[group[0]] + " Hundred "
            
            group = group[1:]
        
        if len(group) == 2:
            ten = int(group[0])
            if ten == 1:
                result += teens_map[group]
                return result
            elif ten >= 2:
                result += tens_map[str(ten)]
            group = group[1:]
        
        result += uni_map[group[-1]]

        return result.strip()

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""

        groups = self.subdivide_num(num)
        for en, group in enumerate(groups):
            group_str = self.translate_group(group)
            result += group_str
            if group_str != "":
                result += th_map[len(groups) - en - 1]
            print(group, group_str)

        if len(result) == 0:
            return "Zero"

        return result.strip()
        