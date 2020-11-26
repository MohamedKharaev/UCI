import re, traceback, keyword
from keyword import kwlist

def pnamedtuple(type_name, field_names, mutable=False):
    def show_listing(s):
        for l,t in enumerate(s.split('\n'), 1):
            print('{line: >4} {text}'.format(line = l, text = t.rstrip()))
        
    def filter_unique(l):
        temp_l = []
        for value in l:
            if value not in temp_l:
                temp_l.append(value)
        return temp_l
    
    def get_init():
        return_str = '\tdef __init__(self, ' + ', '.join(field_names) + '):\n'
        for field in field_names:
            return_str += '\t\tself.' + field + ' = ' + field + '\n'
        return_str += '\t\tself._fields = ' + str(field_names) + '\n'
        return_str += '\t\tself._mutable = ' + str(mutable) + '\n'
        return return_str
    
    def get_repr():
        return_str = '\tdef __repr__(self):\n\t\treturn \'' + type_name + '('
        return_str += ','.join([(field + '={' + field + '}') for field in field_names])
        return_str += ')\'.format('
        return_str += ','.join([(field + '=self.' + field) for field in field_names])
        return_str += ')\n'
        return return_str
    
    def get_getmethods():
        return_str = ''
        for field in field_names:
            return_str += '\tdef get_' + field + '(self):\n'
            return_str += '\t\treturn self.' + field + '\n'
        return return_str
    
    def get_getitem():
        return '''\tdef __getitem__(self, index):
            if type(index) is int:
                if len(self._fields) > index:
                    return self.__dict__[self._fields[index]]
                else:
                    raise IndexError()
            elif type(index) is str:
                if index in self.__dict__:
                    return self.__dict__[index]
                else:
                    raise IndexError()
            else:
                raise IndexError()\n'''
            
    def get_equals():
        return '''\tdef __eq__(self, right):
            if type(right) is type(self):
                for i in range(len(self._fields)):
                    if self[i] != right[i]:
                        return False
                return True
            return False\n'''
    
    def get__replace():
        return_str = '''\tdef _replace(self, **kargs):
            for arg in kargs:
                if arg.split('=')[0] not in self.__dict__:
                    raise TypeError
            if self._mutable:
                for arg in kargs:
                    variable, value = arg.split('=')
                    self.__dict__[variable] = value
                return self
            else:
                new_obj = copy.deepcopy(self)
                for arg in kargs:
                    variable, value = arg.split('=')
                    new_obj.__dict__[variable] = value
                return new_obj\n'''
        return return_str
    
    
    # put your code here
    # bind class_definition (used below) to the string constructed for the class
    name_re = '^[A-Za-z]\w*$'
        
    if type(type_name) is not str:
        raise SyntaxError('pcollection, "pnamedtuple", type_name must be a str')
    if type_name in kwlist:
        raise SyntaxError('pcollections, "pnamedtuple", type_name can not be a keyword')
    if re.match(name_re, type_name) == None:
        raise SyntaxError('pcollection, "pnamedtuple", invalid type_name name')
    
    
        
        
    if type(field_names) is str:
        if ',' in field_names:
            field_names = [field.strip() for field in field_names.split(',')]
        else:
            field_names = field_names.split()
    
    if type(field_names) is not list:
            raise SyntaxError('pcollection, "pnamedtuple", invalid type for field_names')    
    
    field_names = filter_unique(field_names)
    
    for field_name in field_names:
        if re.match(name_re, field_name) == None:
            raise SyntaxError('pcollection, "pnamedtuple", invalid field_names name')
        if field_name in kwlist:
            raise SyntaxError('pcollections, "pnamedtuple", field_names can not be a keyword')
        
    class_definition = 'import copy\nclass ' + type_name + ':\n' + get_init() + get_repr() + get_getmethods() + get__replace() + get_getitem() + get_equals()
    
    

    # For initial debugging, always show the source code of the class
    # show_listing(class_definition)
    
    # Execute the class_definition string in a local namespace; then, bind the
    #   name source_code in its dictionary to the class_defintion; return the
    #   class object created; if there is a syntax error, list the class and
    #   also show the error
    name_space = dict(__name__='pnamedtuple_{type}'.format(type = type_name))
    try:
        exec(class_definition,name_space)
        name_space[type_name].source_code = class_definition
    except(TypeError, SyntaxError):
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':
    # Test pnamedtuple below: e.g., Point = pnamedtuple('Point', 'x y')
    Point = pnamedtuple('Point', 'x y')
    import driver
    driver.driver()
