from goody import type_as_str
import inspect

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value, check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation():
    # set the class attribute below to True for checking to occur
    checking_on  = True
  
    # self._checking_on must also be true for checking to occur
    def __init__(self, f):
        self._f = f
        self._checking_on = True
        
    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)
        def c_listtuple():
            if type(value) is not type(annot):
                raise AssertionError('''AssertionError: '{}' failed annotation check(wrong type): value = {} 
                    was type {} ... should be type {}\n'''.format(str(param), str(value), type_as_str(value), annot[0].__name__) + check_history)
            elif len(annot) == 1:
                for i in range(len(value)):
                    self.check(param, annot[0], value[i], check_history)
            else:
                if len(annot) != len(value):
                    raise AssertionError('''AssertionError: '{}' failed annotation check(wrong number of elements): value = {}
                        annotation had {} elements{}\n'''.format(str(param), str(value), type_as_str(value), len(annot), annot[0].__name__) + check_history)
                for i in range(len(annot)):
                    self.check(param, annot[i], value[i], check_history)
                
        
        def c_dict():
            if not isinstance(value, dict):
                raise AssertionError('''AssertionError: '{}' failed annotation check(wrong type): value = {} 
                    was type {} ... should be type {}\n'''.format(str(param), str(value), type_as_str(value), list(annot)[0].__name__) + check_history)
            elif len(annot) != 1:
                raise AssertionError('''AssertionError: '{}' annotation inconsistency: dict should have 1 value but had {}
                    annotation = {}'''.format(str(param), len(annot), str(annot)) + check_history)
            else:
                for key, key_value in value.items():
                    self.check(param, list(annot.keys())[0], key, check_history)
                    self.check(param, list(annot.values())[0], key_value, check_history)
            
        def c_set():
            if not isinstance(value, set) or not isinstance(value, frozenset):
                raise AssertionError('''AssertionError: '{}' failed annotation check(wrong type): value = {} 
                    was type {} ... should be type {}\n'''.format(str(param), str(value), type_as_str(value), list(annot)[0].__name__) + check_history)
            elif len(annot) != 1:
                raise AssertionError('''AssertionError: '{}' annotation inconsistency: set should have 1 value but had {}
                    annotation = {}'''.format(str(param), len(annot), str(annot)) + check_history)
            else:
                for val in value:
                    self.check(param, list(annot)[0], val, check_history)
    
        def c_func():
            if len(annot.__code__.co_varnames) > 1:
                raise AssertionError('''AssertionError: '{}' annotation inconsistency: predicate should have 1 parameter but had {}
                    predicate = {}\n'''.format(str(param), len(annot.__code__.co_varnames), annot) + check_history)
            else:
                try:
                    if annot(value) == False:
                        raise AssertionError()
                except():
                    raise AssertionError('''AssertionError: '{}' failed annotation check: value = {}
                        predicate = {}\n'''.format(str(param), value, annot) + check_history)
        
        def c_object():
            try:
                value.__check_annotation__(self.check, param, value, check_history)
            except:
                raise AssertionError('''AssertionError: '{}' annotation undecipherable: {}\n'''.format(str(param), value) + check_history)
            
            
        if annot is None:
            pass
        elif isinstance(annot, type):
            if not isinstance(value, annot):
                raise AssertionError('''AssertionError: '{}' failed annotation check(wrong type): value = {} 
                    was type {} ... should be type {}\n'''.format(str(param), str(value), type_as_str(value), annot.__name__) + check_history)      
        elif isinstance(annot, list) or isinstance(annot, tuple):
            c_listtuple()
        elif isinstance(annot, dict):
            c_dict()
        elif isinstance(annot, set):
            c_set()
        elif isinstance(annot, frozenset):
            c_set()
        elif callable(annot):
            c_func()
        else:
            c_object()
        # Decode your annotation next; then check against argument
        
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):
        
        # Return a dictionary of the parameter/argument bindings (actually an
        #    ordereddict: the order parameters appear in the function's header)
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if param.name  not in  bound_f_signature.arguments:
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments

        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        if not self.checking_on or not self._checking_on:
            return self._f(*args, **kargs)
        
        pars = param_arg_bindings()
        anns = self._f.__annotations__
        
        try:
            # Check the annotation for every parameter (if there is one)
            for par in pars:
                if par in anns:
                    self.check(par, anns[par], pars[par])
            # Compute/remember the value of the decorated function
            func_value = self._f(*args, **kargs)
            # If 'return' is in the annotation, check it
            if 'return' in anns:
                pars['_return'] = func_value
                self.check('return', anns['return'], pars['_return'])
            # Return the decorated answer
            return func_value
            
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
            #print(80*'-')
            #for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
            #    print(l.rstrip())
            #print(80*'-')
            raise




  
if __name__ == '__main__':     
    # an example of testing a simple annotation  
    #def f(x:int): pass
    #f = Check_Annotation(f)
    #f(3)
    #f('a')
           
    import driver
    driver.driver()
