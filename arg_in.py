def validator(fn1, string):

  def ttt(fn2):

    def inner(*args, **kwargs):
      if fn2(*args, **kwargs) in fn1:
        return fn2(*args, **kwargs)
      else:
        return string
    return inner

  return ttt


def arg_in(lst):
  return lst


@validator(arg_in([1, 2, 3]), "error")
def example(x):
  return x


example(1)
example(0)
