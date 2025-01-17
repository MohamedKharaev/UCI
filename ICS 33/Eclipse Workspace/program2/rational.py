from goody import irange, type_as_str
import math
import inspect

class Rational:
    @staticmethod
    # Called as Rational._gcd(...); no self parameter
    # Helper method computes the Greatest Common Divisor of x and y
    def _gcd(x : int, y : int) -> int:
        assert type(x) is int and type(y) is int and x >= 0 and y >= 0,\
          'Rational._gcd: x('+str(x)+') and y('+str(y)+') must be integers >= 0'
        while y != 0:
            x, y = y, x % y
        return x
    
    @staticmethod
    # Called as Rational._validate_arithmetic(..); no self parameter
    # Helper method raises exception with appropriate message if type(v) is not
    #   in the set of types t; the message includes the values of the strings
    #   op (operator), lt (left type) and rt (right type)
    # An example call (from my __add__ method), which checks whether the type of
    #   right is a Rational or int is...
    # Rational._validate_arithmetic(right, {Rational,int},'+','Rational',type_as_str(right))
    def _validate_arithmetic(v : object, t : {type}, op : str, left_type : str, right_type : str):
        if type(v) not in t:
            raise TypeError('unsupported operand type(s) for '+op+
                            ': \''+left_type+'\' and \''+right_type+'\'')        

    @staticmethod
    # Called as Rational._validate_relational(..); no self parameter
    # Helper method raises exception with appropriate message if type(v) is not
    #   in the set of types t; the message includes the values of the strings
    #   op (operator), and rt (right type)
    def _validate_relational(v : object, t : {type}, op : str, right_type : str):
        if type(v) not in t:
            raise TypeError('unorderable types: '+
                            'Rational() '+op+' '+right_type+'()') 
                   

    # Put all other methods here
    def __init__(self, num = 0, denom = 1):
        assert (type(num), type(denom)) == (int, int), ('Rational.__init__, unsopported parameter types (num: ' +
                                                      type_as_str(num) + ') and (denom: ' + type_as_str(denom) + ')')
        assert denom != 0, 'Rational.__init__, denom cannot be equal to 0 '
        if num == 0:
            self.num = 0
            self.denom = 1
        else:
            self.num = num // self._gcd(abs(num), abs(denom))
            self.denom = denom // self._gcd(abs(num), abs(denom))
            
        if self.denom < 0:
            self.num *= -1
            self.denom *= -1
            
            
    def __str__(self):
        return (str(self.num) + '/' + str(self.denom))
    
    def __repr__(self):
        return ('Rational(' + str(self.num) + ',' + str(self.denom) + ')')
    
    def __bool__(self):
        return self.num != 0
    
    def __add__(self, right):
        Rational._validate_arithmetic(right, {Rational,int},'+','Rational',type_as_str(right))
        if type(right) is int:
            right = Rational(right)
        return Rational( (self.num * right.denom + right.num * self.denom), (self.denom * right.denom) )
    
    def __radd__(self, left):
        return self.__add__(left)
    
    def __pow__(self, right):
        Rational._validate_arithmetic(right, {int},'**','Rational',type_as_str(right))
        if right < 0:
            return Rational(self.denom ** (-1 * right), self.num ** (-1 * right) )
        return Rational(self.num ** right, self.denom ** right)
    
    def __sub__(self, right):
        Rational._validate_arithmetic(right, {Rational,int},'-','Rational',type_as_str(right))
        if type(right) is int:
            right = Rational(right)
        return Rational( (self.num * right.denom - right.num * self.denom), (self.denom * right.denom) )
    
    def __rsub__(self, left):
        Rational._validate_arithmetic(left, {Rational,int},'-','Rational',type_as_str(left))
        if type(left) is int:
            left = Rational(left)
        return Rational( (left.num * self.denom - self.num * left.denom), (self.denom * left.denom) )

    def __mul__(self, right):
        Rational._validate_arithmetic(right, {Rational,int},'*','Rational',type_as_str(right))
        if type(right) is int:
            right = Rational(right)
        return Rational(self.num * right.num, self.denom * right.denom)
    
    def __rmul__(self, left):
        return self.__mul__(left)
    
    def __gt__(self, right):
        Rational._validate_relational(right, {Rational, int}, '>', type_as_str(right))
        if type(right) is int:
            right = Rational(right)
        return ((self.num / self.denom) > (right.num / right.denom))
    
    def __ge__(self, right):
        return self.__gt__(right) or self.__eq__(right)
    
    def __lt__(self, right):
        Rational._validate_relational(right, {Rational, int}, '<', type_as_str(right))
        if type(right) is int:
            right = Rational(right)
        return ((self.num / self.denom) < (right.num / right.denom))
    
    def __le__(self, right):
        return self.__lt__(right) or self.__eq__(right)

    
    def __eq__(self, right):
        Rational._validate_relational(right, {Rational, int}, '==', type_as_str(right))
        if type(right) is int:
            right = Rational(right)
        return ((self.num / self.denom) == (right.num / right.denom))
    
    def __abs__(self):
        if self.num < 0:
            return Rational(self.num * -1, self.denom)
        else:
            return self
        
    def __neg__(self):
        return Rational(self.num * -1, self.denom)
    
    def __pos__(self):
        return self
    
    def __truediv__(self, right):
        Rational._validate_arithmetic(right, {Rational,int},'/','Rational',type_as_str(right))
        if type(right) is int:
            right = Rational(right)
        return Rational(self.num * right.denom, self.denom * right.num)
    
    def __rtruediv__(self, left):
        Rational._validate_arithmetic(left, {Rational,int},'-','Rational',type_as_str(left))
        if type(left) is int:
            left = Rational(left)
        return Rational(left.num * self.denom, left.denom * self.num)
    
    def __getitem__(self, index):
        if type(index) is int:
            if index == 0:
                return self.num
            elif index == 1:
                return self.denom
        if type(index) is str:
            if 'numerator'.startswith(index.lower()):
                return self.num
            elif 'denominator'.startswith(index.lower()):
                return self.denom
        raise TypeError('List1.__getitem__ index('+str(index)+') must be int or str')
        
        
    def __setattr__(self, name, value):
        calling = inspect.stack()[1]
        if calling.function == '__init__':
            self.__dict__[str(name)] = value
        else:
            raise NameError('Rational.__setattr__ values can only be set in the __init__ method')

    def __call__(self, x):
        return_str = '' if self.num > 0 else '-'
        return_str += str(self.num // self.denom)
        return_str += '.'
        for dec_place in irange(1, x):
            return_str += str((self.num * (10 ** dec_place)) // self.denom)[-1:]
        return return_str
        
        
    
# e ~ 1/0! + 1/1! + 1/2! + 1/3! ... 1/n!
def compute_e(n):
    answer = Rational(1)
    for i in irange(1,n):
        answer += Rational(1,math.factorial(i))
    return answer

# Newton: pi = 6*arcsin(1/2); see the arcsin series at http://mathforum.org/library/drmath/view/54137.html
# Check your results at http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html
#   also see http://www.numberworld.org/misc_runs/pi-5t/details.html
def compute_pi(n):
    def prod(r):
        answer = 1
        for i in r:
            answer *= i
        return answer
    
    answer = Rational(1,2)
    x      = Rational(1,2)
    for i in irange(1,n):
        big = 2*i+1
        answer += Rational(prod(range(1,big,2)),prod(range(2,big,2)))*x**big/big       
    return 6*answer


if __name__ == '__main__':
    #Simple tests before running driver
    print(Rational._gcd(10, 1))
    #x = Rational(8,29) 
    #print(x+x)
    #print(2*x)
    #print(x(30))
    
    print()
    import driver    
    driver.default_file_name = 'bsc2.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
