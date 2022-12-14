class ktools:
  def m(self):
    """Shorthand for move"""
    move()

    def tl(self):
      """Shorthand for turn_left"""
      turn_left()

    def tr(self):
      """Turn right"""
      self.tl()
      self.tl()
      self.tl()

    def ta(self):
      """Turn Around"""
      self.tl()
      self.tl()

    def pick(self):
      """Pick Beeper"""
      pick_beeper()

    def put(self):
      """Put Beeper"""
      put_beeper()

    def put2(self):
      """Put 2 beepers in a line"""
      self.put()
      self.m()
      self.put()

    def put5(self):
      """Put 5 beepers in a line"""
      self.put2()
      self.m()
      self.put2()
      self.m()
      self.put2()

    def fic(self):
      """Front is Clear"""
      return front_is_clear()

    def fib(self):
      """Front Is Blocked"""
      return not self.fic()

    def ric(self):
      """Right is clear"""
    self.tr()
    if self.fic():
      self.tl()
      return True
      self.tl()
      return False
   
   
    def rib(self):
      """Right is Blocked"""
      return not self.ric()

    def mazemove(self):
      """Maze move"""
      if self.fib():
        self.tl()
      else:
        self.m()
        if self.ric():
          self.tr()
          self.m()
          if self.ric():
            self.tr()
            self.m()
      pass

    def mm(self, num):
      """Move multiple"""
      for number in range(num):
        self.m()

    def pickm(self, num):
      """Pick multiple"""
      for i in range(num-1):
        self.pick()
        self.m()
      self.pick()

    def putm(self, num):
      """Put multiple"""
      for _ in range(num-1):
        self.put()
        self.m()
      self.put()
     


def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.m()
    kt.tl()
    kt.m()
    kt.put()
    kt.ta()
    kt.m()
    kt.tl()
    kt.mm(5)
    kt.tl()
    kt.m()
    kt.put()
    kt.ta()
    kt.m()
    kt.tl()
    kt.mm(3)
    pass


if __name__ == "__main__":
    run_karel_program()