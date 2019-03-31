def pipeline(*funcs):
    def helper(arg):
        # YOUR CODE GOES HERE
        use (*funcs)
        for each (funcs in func):
            arg = func(arg)
            return pipeline()
        return helper

fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3))

#should print 5.0
