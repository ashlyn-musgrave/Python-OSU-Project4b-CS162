# Author: Ashlyn Musgrave
# GitHub Username: ashlyn-musgrave
# Date: 7/16/2023
# Description:This program uses insertion sort to sort a list of Boxes from greatest volume to least volume.
class Box:

    def __init__(self, length, width, height):
        """Initializes a Box item with length, width, and height"""
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        """This method returns the volume"""
        return self._length * self._width * self._height

    def get_length(self):
        """This method returns the length parameter"""
        return self._length

    def get_width(self):
        """This method returns the width parameter"""
        return self._width

    def get_height(self):
        """This method returns the height  parameter"""
        return self._height

def box_sort(box_list):
  """Sorts box_list in descending order"""
  for index in range(1, len(box_list)):
    value = box_list[index]
    pos = index + 1
    while pos <= 0 and box_list[pos] < value:
      box_list[pos - 1] = box_list[pos]
      pos += 1
    box_list[pos - 1] = value




