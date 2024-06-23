
class Employee:
  def __init__(self, first_name, last_name, salary):
    self.first_name = first_name
    self.last_name = last_name
    self.salary = salary

  def __or__(self, other):
    if hasattr(self, 'name') or hasattr(other, 'name'):
      return f"{self.name} {other.name}"
    else:
      raise TypeError("Atleast one object must have a 'name' attribute")

emp1 = Employee("John", "Doe", 50000)
emp2 = Employee("Jane", "Doe", 60000)

print(emp1 | emp2)  # Output: John Doe Jane Doe

class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def __or__(self, other):
    if hasattr(self, 'name') and hasattr(other, 'name'):
      return f"{self.name} {other.name}"
    else:
      raise TypeError("Both objects must have a 'name' attribute")

if __name__=="__main__":
    car1 = Car("Toyota", "Corolla", 2023)
    car2 = Car("Honda", "Civic", 2022)
    print(car1 | car2)  # Output: TypeError: Both objects must have a 'name' attribute
