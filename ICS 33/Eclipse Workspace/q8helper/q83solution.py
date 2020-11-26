from   bag import Bag
import unittest  # use unittest.TestCase
import random    # use random.shuffle, random.randint
from goody import irange

#random.shuffle(alist) mutates its alist argument into a random permutation
#random.randint(1,10)  returns random number in the range 1-10 inclusive


class Test_Bag(unittest.TestCase):
    def setUp(self):
        self.alist = ['d','a','b','d','c','b','d']
        self.bag = Bag(self.alist)
    
    def testlen(self):
        assert len(self.bag) == 7
        random.shuffle(self.alist)
        for i in irange(1, len(self.alist)):
            self.bag.remove(self.alist[i - 1])
            assert len(self.bag) == 7 - i, '{}, {}'.format(i, self.bag.counts)

    def testunique(self):
        assert self.bag.unique() == 4
        random.shuffle(self.alist)
        for i in irange(1, len(self.alist)):
            self.bag.remove(self.alist[i - 1])
            assert self.bag.unique() == len(self.bag.counts)
            
    def testcontains(self):
        for letter in ['a', 'b', 'c']:
            assert self.bag.__contains__(letter)
        assert not self.bag.__contains__('x')
    
    def testcount(self):
        assert list(map(lambda x: self.bag.count(x), ['a', 'b', 'c', 'd', 'x'])) == [1, 2, 1, 3, 0]
        random.shuffle(self.alist)
        for i in irange(1, len(self.alist)):
            self.bag.remove(self.alist[i - 1])
            assert sum([self.bag.count(x) for x in self.bag.counts]) == len(self.alist) - i
        
    def testequals(self):
        rand_list = []
        for i in range(1000):
            rand_list.append(random.randint(1, 10))
        bag = Bag(rand_list)
        random.shuffle(rand_list)
        bag2 = Bag(rand_list)
        assert bag == bag2
        bag.remove(rand_list[0])
        assert bag != bag2
        
    def testadd(self):
        rand_list = []
        for i in range(1000):
            rand_list.append(random.randint(1, 10))
        bag = Bag(rand_list)
        bag2 = Bag()
        random.shuffle(rand_list)
        for value in rand_list:
            bag2.add(value)
        assert bag == bag2
        
    def testremove(self):
        rand_list = []
        for i in range(1000):
            rand_list.append(random.randint(1, 10))
        bag = Bag(rand_list)
        try:
            bag.remove(62)
        except ValueError:
            pass
        bag2 = Bag(rand_list)
        random.shuffle(rand_list)
        for value in rand_list:
            bag2.add(value)
        for value in rand_list:
            bag2.remove(value)
        assert bag == bag2
        
        
        