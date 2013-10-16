import sys

class Matrix:

    def __init__(self, n, m=None, values=[]):
        if m == None:
            m = n

        self.n = n
        self.m = m

        values = map(lambda x : float(x), values)
        if len(values) == self.n*self.m:
            self.values = values[0:self.n*self.m]
        else:
            sys.exit("Error, values argument of incorrect dimension.")



    def __str__(self):
        retstr = ""

        retstr += "\n\n"
        retstr += "[\n"

        for i in range(0, self.n):
            for j in range(0, self.m):
                retstr += '{: 14,.6f}'.format(self.values[self.m*i + j])
                retstr += ' , '
            retstr += "\n"

        retstr += "]\n"

        return retstr



    def __repr__(self):
        return self.__str__()


    def __getitem__(self, a):
        return self.values[a[0]*self.m + a[1]]



    def __setitem__(self, a, b):
        self.values[(a[0] % self.n)*self.m + a[1] % self.m] = b



    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.n != other.n or self.m != other.m:
                raise ValueError("Cannot add, matrix dimensions do not match.")

            return Matrix(self.n, self.m, [self.values[k] + other.values[k] for k in range(0, self.n*self.m)])

        else:
            raise TypeError("Cannot add matrix and object of type " + str(type(other)))



    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.n != other.n or self.m != other.m:
                raise ValueError("Cannot subtract, matrix dimensions do not match.")

            return Matrix(self.n, self.m, [self.values[k] - other.values[k] for k in range(0, self.n*self.m)])

        else:
            raise TypeError("Cannot subtract matrix and object of type " + str(type(other)))



    def __mul__(self, other):
        if isinstance(other, (int, float, long)):
            return Matrix(self.n, self.m, [other*x for x in self.values])

        elif isinstance(other, Matrix):
            if self.n != other.m or self.m != other.n:
                raise ValueError("Cannot multiply, matrix dimensions are incompatable.")

            return Matrix(self.n, self.n, [sum(map(lambda x : x[0]*x[1], zip(self.get_row(k/self.n), other.get_col(k)))) for k in range(0, self.n*self.n)])

        else:
            raise TypeError("Cannot multiply matrix and object of type " + str(type(other)))
   

            
    def __rmul__(self, other):
        if isinstance(other, (int, float, long)):
            return Matrix(self.n, self.m, [other*x for x in self.values])

        elif isinstance(other, Matrix):
            if self.n != other.m or self.m != other.n:
                raise ValueError("Cannot multiply, matrix dimensions are incompatable.")

            return Matrix(self.m, self.m, [sum(map(lambda x : x[0]*x[1], zip(other.get_row(k/other.n), self.get_col(k)))) for k in range(0, self.m*self.m)])

        else:
            raise TypeError("Cannot multiply matrix and object of type " + str(type(other)))



    def transpose(self):
        return Matrix(self.m, self.n, [self.values[(k%self.n)*self.m + (k/self.n)] for k in range(0, self.n*self.m)])



    def get_row(self, row):
        row = row % self.n
        return self.values[row*self.m:(row+1)*self.m]



    def get_col(self, col):
        col = col % self.m
        values = []
        for i in range(0, self.n):
            values.append(self.values[i*self.m + col])
        return values



class NullMatrix(Matrix):

    def __init__(self, n, m=None):
        if m == None:
            m = n
        Matrix.__init__(self, n, m, [0]*n*m)



class IdentityMatrix(Matrix):

    def __init__(self, dim):
        values = [0]*(dim ** 2)
        for i in range(0, dim):
            values[i*dim + i] = 1
        Matrix.__init__(self, dim, dim, values)
