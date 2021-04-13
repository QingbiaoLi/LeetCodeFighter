

# Binary search
class Solution:
  def mySqrt(self, a):
    l = 1
    r = a
    while l <= r:
      m = l + (r - l) // 2
      if m * m > a:
        r = m - 1
      else:
        l = m + 1
    return r




class Solution:
  def mySqrt(self, a):
    x = a
    while x * x > a:
      x = (x + a // x) // 2
    return x