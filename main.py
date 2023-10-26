def enforce(*types):
    def decorator(f):
            def new_func(*args, **kwargs):
                newargs= []
                for (a, t) in zip(args, types):
                    newargs.append( t(a))
                return f(*newargs, **kwargs)
            return new_func
    return decorator

@enforce(str, int)
def repeat_msg (msg, times):
    for time in range(times):
        print (msg)
        
repeat_msg ("hello", 2)
# hello
# hello
repeat_msg ("hello", '2')
# hello
# hello
repeat_msg ("hello", [2,2]) # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
