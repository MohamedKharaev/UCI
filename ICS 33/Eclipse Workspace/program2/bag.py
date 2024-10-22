from collections import defaultdict

class Bag:
    def __init__(self, itr = []):
        self.bag_items = defaultdict(int)
        for item in itr:
            self.bag_items[item] += 1
    
    def __repr__(self):
        bag_list = []
        for item, amount in self.bag_items.items():
            bag_list.extend([item] * amount)
        return ('Bag(' + str(bag_list) + ')')
    
    def __str__(self):
        return ('Bag(' + ', '.join([ (str(item) + '[' + str(self.bag_items[item]) + ']') for item in self.bag_items]) + ')')        

    def __len__(self):
        return sum(self.bag_items.values())
    
    def unique(self):
        return len(self.bag_items)
    
    def __contains__(self, item):
        if item in self.bag_items:
            return True
        return False
    
    def count(self, item):
        if item in self.bag_items:
            return self.bag_items[item]
        return 0
    
    def add(self, item):
        self.bag_items[item] += 1
        
    def __add__(self, bag2):
        if type(bag2) != type(self):
            raise TypeError('Unsupported addition. Both objects must be bags')
        bag_list = []
        for item, amount in self.bag_items.items():
            bag_list.extend([item] * amount)
        for item, amount in bag2.bag_items.items():
            bag_list.extend([item] * amount)
        return Bag(bag_list)    
        
    def remove(self, item):
        if item in self.bag_items:
            self.bag_items[item] -= 1
            if self.bag_items[item] == 0:
                self.bag_items.pop(item)
        else:
            raise ValueError('there is no ' + str(item) + 'in the bag')
        
    def __eq__(self, right):
        if type(right) == type(self):
            if self.bag_items == right.bag_items:
                return True
        return False
    
    def __iter__(self):
        bag_copy = []
        for item, amount in self.bag_items.items():
            bag_copy.extend([item] * amount)
        return iter(bag_copy)
        
if __name__ == '__main__':
    #Put your own test code here to test Bag before doing bsc tests
    print('Start simple testing')

    import driver
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_exception =True
#     driver.default_show_exception_message =True
#     driver.default_show_traceback =True
    driver.driver()
