def validator(fn1, string):
    def ttt(fn2):
        def inner(*args, **kwargs): 
            if "greater_than" in used:
                used.clear()
                if fn1 < fn2(*args, **kwargs):
                    print(fn2(*args, **kwargs))
                else:
                    print(string)
                    
            if "less_than" in used:
                used.clear()
                if fn1 > fn2(*args, **kwargs):
                    print(fn2(*args, **kwargs))
                else:
                    print(string)
                    
            if "arg_in" in used:
                used.clear()
                if fn2(*args, **kwargs) in fn1:
                    print(fn2(*args, **kwargs))
                else:
                    print(string)
                    
            if "starts_with" in used:
                used.clear()
                if fn2(*args, **kwargs)[:len(fn1)] == fn1:
                    print(fn2(*args, **kwargs))
                else:
                    print(string)
        return inner
    return ttt

used = []

def greater_than(x):
    used.append("greater_than")
    return x

def less_than(x):
    used.append("less_than")
    return x

def arg_in(lst):
    used.append("arg_in")
    return lst

def starts_with(string):
    used.append("starts_with")
    return string


@validator(less_than(0), "error")
def example(x):
    return x
