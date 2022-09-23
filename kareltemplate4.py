from stanfordkarel import *


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

  def put2(self):
    """put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()
    

  def put5(self):  
    """put 5 beepersa in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def h(self):
    """print H using beepera"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()


def mm(self, num):
    """ Karel code goes here! """
  for number in range(0, num):
    self.m()

def putn(self, num):
    """put multipe"""
    for i in range (num - 1):
    self.put()
    self.m()
    self.put()

def putn(self, num):
    """put multipe"""
    for _ in range (num - 1):
    self.pick()
    self.m()
    self.pick()
  
   pass


if __name__ == "__main__":
    run_karel_program()