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
    self.tr()
    self.tr()
    self.tr()
  
   def ta(self):
    """turn around"""
    self.ta()
    self.ta()
  
   def pick(self):
    """pick beeper"""
    pick_beeper()

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
    """print h using beepers"""
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
    self.m()


def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.h()
  
    pass


if __name__ == "__main__":
   run_karel_program()