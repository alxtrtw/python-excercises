roman_symbol_map = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}

class Solution(object):
    
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        result = ""
        sorted_keys = sorted(roman_symbol_map.keys(), reverse=True)
        temp_num = num
        print("Originally ", temp_num)
        while temp_num > 0:
            for k in sorted_keys:
                if k <= temp_num:
                    temp_num -= k
                    result += roman_symbol_map[k]
                    break
            print(temp_num, result)

        return result
