#!/usr/bin/env python3

class MyString:
  def __init__(self, value= None):
    self.value = value
  
  def get_value(self):
    return self._value 
  
  def set_value(self, value):
    if isinstance(value, str):
      self._value = value
    
    else:
      print("The value must be a string.")
  
  value = property(get_value, set_value)

  def is_sentence(self):
    if self._value and self._value.endswith("."):
      return True
    else:
      return False
    
  def is_question(self):
    if self._value and self._value.endswith("?"):
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self._value and self._value.endswith("!"):
      return True
    else:
      return False

my_string = MyString("I love singing")
my_string.value = "Do I love singing!"
print(my_string.is_exclamation())
# print(my_string.value)