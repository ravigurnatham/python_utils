#this code will run if the object is called directly after createion or at any point of time
import datetime
class Timed:
  def __init__(self):
    self.created_at = datetime.datetime.now()

  def __call__(self):
    print("Object created at:", self.created_at)

timed_object = Timed()
timed_object()
