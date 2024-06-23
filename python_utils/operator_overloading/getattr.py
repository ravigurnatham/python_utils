#write operator overloading for __getattr__ ?

class MyClass:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __getattr__(self, attr):
    if attr == "fullname":
      return self.name + " " + self.age
    else:
      raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr}'")
  

if __name__=="__main__":
    my_class = MyClass("John", "Doe")
    print(my_class.name)  
    print(my_class.fullname)  
    print(my_class.address)  # Raises AttributeError
