class Design(object):
    """docstring for Design"""
    def __init__(self, f=0, b=0, ls=0, rs=0, pm='sp'):
        self.f = f
        self.b = b
        self.ls = ls
        self.rs = rs
        self.pm = pm
        self.locs = sum(map(lambda x: (x > 0),
                        [self.f, self.b, self.ls, self.rs]))

    def print_locs(self):
        print(self.locs)

class PrintArea(Object):
