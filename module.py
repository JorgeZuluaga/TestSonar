import numpy

class Series(object):

    def __init__(self,N,a):
        self.N=N
        self.a=a

    def get_value(self,x):
        suma=0
        for n in range(self.N):
            suma+=self.a[n]*x**n
        return suma

    def get_derivative(self,x):
        deriv=0
        for n in range(1,self.N):
            deriv+=n*self.a[n]*x**(n-1)
        return deriv

if __name__=="__main__":
    s=Series(3,[1,1/2,1/6])
    print(s.get_derivative(1))
    
