def validator(fn1, string):

  def ttt(fn2):

    def inner(*args, **kwargs):
      if fn2(*args, **kwargs)[:len(fn1)] == fn1:
        return fn2(*args, **kwargs)
      else:
        return string
    return inner

  return ttt


def starts_with(string):
  return string


@validator(starts_with('ddd'), "error")
def example(x):
  return x


example("dddd12")
example("sdfn")
