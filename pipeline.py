def pipeline(*funcs):
    def helper(arg):
        # YOUR CODE GOES HERE
        for (arg) in funcs:
            return pipeline(arg)

    return helper

# I did not  get this to work, I missed the class where pipelines were discussed.
# I'll continue working on this while the results are being examined, sorry about that!

fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3))

#should print 5.0
