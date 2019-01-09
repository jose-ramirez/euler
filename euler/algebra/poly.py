class Poly:
  def __init__(self, p):
    self.p = p
    self.deg = len(self.p) - 1

  def coeff(self, i):
    if i > self.deg:
      return 0
    else:
      return self.p[self.deg - i]

  def c(self, p2, r):
    total = 0
    if r == 0:
      return self.coeff(0) * p2.coeff(0)
    else:
      for i in range(r + 1):
        total += self.coeff(i) * p2.coeff(r - i)
    return total

  def mul(self, p2):
    l = [self.c(p2, i) for i in range(self.deg + p2.deg + 1)]
    return Poly(l[::-1])

  def pow(self, exp):
    if exp == 1:
      return self
    else:
      return self.mul(self.pow(exp - 1))