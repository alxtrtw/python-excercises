class Solution(object):
    
    def get_gap_lens(self, n_spaces, n_gaps):
        gap_len = n_spaces // n_gaps
        gap_mod = n_spaces % n_gaps
        gap_lens = [gap_len for _ in range(n_gaps)]
        if gap_mod != 0:
            for i in range(gap_mod):
                gap_lens[i] += 1
        return gap_lens + [0]

    def construct_line(self, words_in_line, maxWidth, fill=False):
        
        wl_len = len(words_in_line)
        print("> ", words_in_line, wl_len == 1, fill)
        if wl_len == 1 or fill:
            return ' '.join(words_in_line).ljust(maxWidth)

        n_gaps = len(words_in_line) - 1
        words_len = sum([len(wl) for wl in words_in_line])
        n_spaces = maxWidth - words_len

        gap_lens = self.get_gap_lens(n_spaces, n_gaps)

        result_line = ""
        for i, w in enumerate(words_in_line):
            result_line += w + ' ' * gap_lens[i]            

        return result_line
    
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        words_len = len(words)
        words_in_line = []
        result_lines = []
        c = 0
        for i, w in enumerate(words):
            l = len(w)
            
            # will the word fit?
            if c + l <= maxWidth:
                # yes, so add the word
                c += l
                words_in_line.append(w)

                # will any more words fit?
                if c + 2 <= maxWidth:
                    # yes, so account for space
                    c += 1
                else:
                    # no, so construct the line
                    result_lines.append(
                        self.construct_line(words_in_line, maxWidth, fill=(i == words_len - 1)))
                    c = 0
                    words_in_line = []

            else:
                # no, so construct the line and start a new one
                result_lines.append(
                    self.construct_line(words_in_line, maxWidth, fill=False))
                c = l + 1
                words_in_line = [w]

        # finished adding words, add extra spaces at the end
        if words_in_line:
            result_lines.append(self.construct_line(words_in_line, maxWidth, fill=True))

        return result_lines