class ktools:
  def m(self):
    """shorthand for move"""
    move()

  def tl(self):
   """turn left"""
   turn_left()

  def tr(self):
    """turn right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
    """turn around"""
    self.tl()
    self.tl()

  def pick(self):
    """pick beeper"""
    pick_beeper()


  def put(self):
    """put beeper"""
    put_beeper()

  def put2(self):
    """put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """put 5 beepers in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def h(self):
    """print it using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m3()
    self.tr()
    self.put5()
    self.ta()
    self.m2()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m2()
    self.tl()
    self.m4()

  def m3(self):
    """move three times"""
    self.m()
    self.m()
    self.m()

  def m2(self):
    """move two times"""
    self.m()
    self.m()

  def m4(self):
    """move four times"""
    self.m()
    self.m()
    self.m()
    self.m()

  def fic(self) -> bool:
    """front is clear"""
    return front_is_clear()

  def fib() -> bool:
    """front is blocked"""
    return not self.fic()
  def ric(self) -> bool:
    """right is clear"""
    self.tr()
    if self.fic():
     self.tl()
    return True  # Immediately exit the function
    self.tl()
    return False

  def rib(self) -> bool:
    """right is blocked"""
    return not self.ric()

  def mazemove(self):
    """maze move"""
    if self.fib():
     self.tl()
    else:  # otherwise...
     self.m()
    if self.ric():
     self.tr()
    self.m()
    if self.ric():
     self.tr()
    self.m()

  def makeO(self):
    """make 0"""
    self.put()
    self.m()
    self.put()
    self.m()
    self.put()
    self.tl()
    self.put5()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.put5()
    self.tl()
    self.m5()

  def mm(self, num):
    """move multiple"""
    for number in range(0, num):
      self.m()

  def putm(self,num):
    """put multiple"""
    for i in range(num - 1):
      self.put()
      self.m()
    self.put()

  def pickm(self,num):
    """pick multiple"""
    for _ in rang(num - 1):
      self.pick()
      self.m()
    self.pick()

  def m5(self):
    """move five times"""
    self.m()
    self.m()
    self.m()
    self.m()
    self.m()
   
    pass

     
def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.tl()
    kt.mm(4)
    kt.ta()
    kt.putm(5)
    kt.tl()
    kt.mm(2)
    kt.makeO()
    kt.makeO()
    kt.makeO()
    kt.makeO()
    kt.makeO()
    kt.makeO()
    kt.makeO()
    kt.makeO()
    kt.makeO()
    kt.makeO()
    kt.makeO()
    kt.makeO()
    kt.makeO()
    kt.makeO()
    kt.makeO()
    kt.makeO()
    kt.makeO()
    kt.makeO()
    kt.makeO()
    pass
  def SOB(self) -> bool:
    """standing on beepers"""
    return beepers_present()

  def jump(self)
    """jump for 510"""
    while self.fic():
      self.m()
    self.tl()
    while.self.rib():
      self.m()
      sefl.tr()
      self.m()
      self.tr()
    while self.fic():
      self.m()
      self.tl()

  def find(self).508():
    """find for 515"""
    while not facing north():
    self.tl()
    self.m()
    self.tl()
    self.m()
    for _ in range(2):
      if not self.508():
      self.m()
      self,tl
      self.m()
    pass


if __name__ == "__main__":
    run_karel_program()
    kt=ktools()
    kt.m()
    ktool.tl()
    kt.m()
    kt.tr()
    kt.m()
    while kt.508():
    kt.pick()
    kt.find()
   pass