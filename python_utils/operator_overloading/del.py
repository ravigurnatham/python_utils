class CustomClass:
  def __init__(self, value):
    self.value = value

  def __del__(self):
    print(f"Object with value {self.value} is being deleted")

obj = CustomClass(10)
del obj
