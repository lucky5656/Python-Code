class A(object):
    def __init__(self, a=0):
        self.a = a
    def get(self):
        return self.a

class B(A):
    def __init__(self, b):
        super(B, self).__init__(b)
    def get(self):
        return super(B, self).get()

if __name__ == '__main__':
    b = B(10)
    print(b.get())
