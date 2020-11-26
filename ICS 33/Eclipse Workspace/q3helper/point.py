import math
from goody import type_as_str

class Point:
    def __init__(self, x: int, y: int, z: int):
        assert [type(x), type(y), type(z)] == [type(0)] * 3, 'Point Class, __init__ method, Parameters are not ints'
        self.x = x
        self.y = y
        self.z = z
        self.coordinates = [x, y, z]

    def __repr__(self):
        return ('Point(' + ','.join([str(num) for num in self.coordinates]) + ')')
    
    def __str__(self):
        return ('(x=' + str(self.x) + ',y=' + str(self.y) + ',z=' + str(self.z) + ')')
    
    def __bool__(self):
        if self.coordinates == [0, 0, 0]:
            return False
        return True
    
    def __add__(self, right):
        if type(right) != type(self):
            raise TypeError('unsupported operand type(s) for +'+
                            ': \''+type_as_str(self)+'\' and \''+type_as_str(right)+'\'')
        new_coords = [(x + y) for x,y in zip(self.coordinates, right.coordinates)]
        return Point(new_coords[0], new_coords[1], new_coords[2])
    
    def __mul__(self, right):
        if type(right) is not int:
            raise TypeError('unsupported operand type(s) for *' + 
                            ': \'' + type_as_str(self)+'\' and \''+type_as_str(right)+'\'')
        return Point(self.x * right, self.y * right, self.z * right)
    
    def __rmul__(self, left):
        return self.__mul__(left)
    
    
    def __lt__(self, right):
        if type(right) in (int, float):
            return math.sqrt(sum([value ** 2 for value in self.coordinates])) < right
        elif type(right) is type(self):
            return math.sqrt(sum([value ** 2 for value in self.coordinates])) < math.sqrt(sum([value ** 2 for value in right.coordinates]))
        else:
            raise TypeError('unsupported operand type(s) for <' + 
                            ': \'' + type_as_str(self)+'\' and \''+type_as_str(right)+'\'')
            
    
    def __getitem__(self, index):
        if type(index) in (int, str):
            if index in (0, 'x'):
                return self.x
            elif index in (1, 'y'):
                return self.y
            elif index in (2, 'z'):
                return self.z
            else:
                raise IndexError(type_as_str(self) + 'index out of range')
        elif type(index) is float:
            raise IndexError(type_as_str(self) + 'index out of range')
        else:
            raise TypeError('unsupported operand type(s) for __getitem__' + 
                            ': \'' + type_as_str(self)+'\' and \''+type_as_str(index)+'\'')
    
    def __call__(self, new_x, new_y, new_z):
        assert [type(new_x), type(new_y), type(new_z)] == [type(0)] * 3, 'Point Class, __call__ method, Parameters are not ints'
        self.x = new_x
        self.y = new_y
        self.z = new_z
        self.coordinates = [new_x, new_y, new_z]

        
if __name__ == '__main__':
    #Simple tests before running driver
    #Put your own test code here to test Point before doing bsc tests
    print('Start simple testing')
    
    print()
    import driver
    
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
