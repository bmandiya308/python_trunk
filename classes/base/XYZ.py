class First(object):
  def __init__(self):
    print("First(): entering")
    super(First, self).__init__()
    print("First(): exiting")
  def extra_def(self):
    print("extra_def_First")
    #super(Third, self).extra_def()
    return
  def name(self):
    return "Bhaskar"

class Second(object):
  def __init__(self):
    print("Second(): entering")
    super(Second, self).__init__()
    print("Second(): exiting")
  def extra_def(self):
      print("extra_def_Second")
      return
  def sirname(self):
   return "Mandiya"

class Third(First, Second):
  def __init__(self):
    print("Third(): entering")
    super(Third, self).__init__()
    print("Third(): exiting")
    super(Third, self).extra_def()
    super(First, self).extra_def()
