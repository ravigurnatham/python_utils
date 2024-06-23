class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    if isinstance(other, Point):
      return Point(self.x + other.x, self.y + other.y)
    else:
      raise TypeError("Invalid operand type for +: 'Point' and '{}'".format(type(other)))

if __name__=="__main__":
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = p1 + p2
    print(p3.x, p3.y)
