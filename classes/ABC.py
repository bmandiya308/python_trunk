class First(object):
  def __init__(self):
    print("First(): entering")
    super(First, self).__init__()
    print("First(): exiting")
  def extra_def(self):
    print("extra_def_First")

class Second(object):
  def __init__(self):
    print("Second(): entering")
    super(Second, self).__init__()
    print("Second(): exiting")
  def extra_def(self):
      print("extra_def_Second")

class Third(First, Second):
  def __init__(self):
    print("Third(): entering")
    super(Third, self).__init__()
    print("Third(): exiting")
    super(Third, self).extra_def(self)
    super(Third, self).extra_def(self)
