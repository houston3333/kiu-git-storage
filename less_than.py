def validator(fn1, string):

  def ttt(fn2):

    def inner(*args, **kwargs):
      if fn1 > fn2(*args, **kwargs):
        return fn2(*args, **kwargs)
      else:
        return string
    return inner

  return ttt


def less_than(x):
  return x


@validator(less_than(0), "error")
def example(x):
  return x


example(100)
example(-100)
