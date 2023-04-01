# http://hplgit.github.io/primer.html/doc/pub/class/._class-readable005.html

from math import sqrt

class Complex(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag
        
    def __add__(self, other):
        """ 
        we may add instances of class Complex and 
        Python's own complex class (complex), since all we need is an object with real and imag attributes.
        """
        # isinstance(object, type) 
        # The isinstance() function returns True if the specified object is of the specified type, otherwise False.
        if isinstance(other, (float,int)):
            other = Complex(other)
        elif not (hasattr(other, 'real') and hasattr(other, 'imag')): #  duck typing
            # hasattr(a, attr)
            # check if an object a has an attribute with name stored in the string attr
            raise TypeError('other must have real and imag attr.')
        return Complex(self.real + other.real,self.imag + other.imag)

    def __radd__(self, other):        # defines other + self
        """
        for the case where the class instance (self) is on the 
        right-hand side of the operator and the other object is on the left-hand side. 
        E.g. w = 4.5 + u
        """
        return self.__add__(other)    # other + self = self + other
    
    def __sub__(self, other):
        if isinstance(other, (float,int)):
            other = Complex(other)
        elif not (hasattr(other, 'real') and hasattr(other, 'imag')):
            raise TypeError('other must have real and imag attr')
        
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __rsub__(self, other):
        if isinstance(other, (float,int)):
            other = Complex(other)
        return other.__sub__(self)
    
    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag, self.imag*other.real + self.real*other.imag)

    def __div__(self, other):
        sr, si, oor, ooi = self.real, self.imag, other.real, other.imag # short forms
        r = float(oor**2 + ooi**2)
        return Complex((sr*oor+si*ooi)/r, (si*oor-sr*ooi)/r)

    def __abs__(self):    
        return sqrt(self.real**2 + self.imag**2)  # operator.abs(obj)

    def __neg__(self):   
        return Complex(-self.real, -self.imag)

    def __eq__(self, other, eps = 1E-14):
        """ eps -> tolerance """
        return abs(self.real - other.real) < eps and abs(self.imag - other.imag) < eps

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        """The __str__() method returns a simpler description 
        with information for the user of the program."""
        return '(%g, %g)' % (self.real, self.imag)

    def __repr__(self):
        """The .__repr__() method returns a detailed description for 
           a programmer who needs to maintain and debug the code. """
        return 'Complex' + str(self)

    def __pow__(self, power):
        raise NotImplementedError('self**power is not yet impl. for Complex') # The raise keyword is used to raise an exception.
    
    def _illegal(self, op):
        print('illegal operation "%s" for complex numbers' % op)

    def __gt__(self, other):  self._illegal('>')
    def __ge__(self, other):  self._illegal('>=')
    def __lt__(self, other):  self._illegal('<')
    def __le__(self, other):  self._illegal('<=')

if __name__ == "__main__":
    c = Complex(1,2)
    a = 1
    print(a - c)
