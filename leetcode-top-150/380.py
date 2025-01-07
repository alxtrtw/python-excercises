import random
import itertools

class RandomizedSet(object):

    rset = None

    def __init__(self):
        self.rset = set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.rset:
            return False
        else:
            self.rset.add(val)
            return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.rset:
            self.rset.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """

        ## best solution found for sampling a set
        ## beats 30% on runtime and 80% on space
        return random.choice(list(self.rset))

        ## 5% 80%
        # random_index = random.randrange(len(self.rset))
        # return next(x for i, x in enumerate(self.rset) if i == random_index) 

        ## 13% 44%
        # return random.sample(self.rset, 1)[0]

        ## 15% 46%
        # random_index = random.randint(0, len(self.rset) - 1)
        # return next(itertools.islice(self.rset, random_index, None))


        