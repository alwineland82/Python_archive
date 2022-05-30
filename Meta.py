class Debugger(object):
    attribute_accesses = []
    method_calls = []


class Meta(type):
    
    def decorator_for_methods(f):
            def new_funk(*args, **kwargs):
                dic = {}
                dic['class'] = args[0].__class__
                dic['method'] = f.__name__
                dic['args'] = args
                dic['kwargs'] = kwargs
                Debugger.method_calls.append(dic)
                decorated_method = f(*args)
                return decorated_method
            return new_funk
            
    def __new__(cls, name, bases, namespace):
        def __setattr__(self, item, value):
            dic = {}
            if item != '__class__':
                dic['action'] = 'set'
                dic['class'] = self.__class__
                dic['attribute'] = item
                dic['value'] = value
                Debugger.attribute_accesses.append(dic)
            return object.__setattr__(self, item, value)    
        namespace.update({'__setattr__': __setattr__})
        def __getattribute__(self, item):
            dic = {}
            if item != '__class__':
                print(self)
                dic['action'] = 'get'
                dic['class'] = self.__class__
                dic['attribute'] = item
                dic['value'] = object.__getattribute__(self, item)
                Debugger.attribute_accesses.append(dic)    
            return object.__getattribute__(self, item)
        namespace.update({'__getattribute__': __getattribute__})
        for i in namespace:
            if namespace[i].__class__.__name__ == 'function' and i not in '__getattribute__' and i not in '__setattr__':
                namespace.update({i: Meta.decorator_for_methods(namespace[i])})
        return super().__new__(cls, name, bases, namespace)
    
    
class Foo(object, metaclass = Meta):
    class_atr = 'class atr'
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def bar(self, v):
        return (self.a, v)
        

foo = Foo(1, 2)
foo.bar(10)


for i in Debugger.attribute_accesses:
    print(i)
print()
for i in Debugger.method_calls:
    print(i)



