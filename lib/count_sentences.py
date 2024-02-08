#!/usr/bin/env python3
import re

class MyString:
  def __init__(self,value="") -> None:
    self._value = value

  def get_value(self):
    return self._value

  def set_value(self,value):
    if isinstance(value,str):
      return self._value
    else:
      print("The value must be a string.")

  value =property(get_value, set_value)

  def is_sentence(self):
    if self._value[-1] == ".":
      return True
    else:
      return False

  def is_question(self):
    if self._value[-1] == "?":
      return True
    else:
      return False

  def is_exclamation(self):
    if self._value[-1] == "!":
      return True
    else:
      return False

  def count_sentences(self):
      delimiters = r"[.!?]"
      sentences = re.split(delimiters, self._value)

      non_empty_sentences = list(filter(lambda x: x.strip() != '', sentences))
      count = len(non_empty_sentences)
      return count