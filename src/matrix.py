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
                retstr += '{:>6,.2f}'.format(self.values[self.m*i + j])
                retstr += ' , '
            retstr += "\n"

        retstr += "]\n"

        return retstr



    def __getitem__(self, a):
        return self.get_row(a)



    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.n != other.n or self.m != other.m:
                sys.exit("Matrix dimensions do not match. Aborting!")

            return Matrix(self.n, self.m, [self.values[k] + other.values[k] for k in range(0, self.n*self.m)])

        else:
            sys.exit("Cannot add matrix and object of type " + str(type(other)))



    def __mul__(self, other):
        if isinstance(other, (int, float, long)):
            return Matrix(self.n, self.m, [other*x for x in self.values])

        elif isinstance(other, Matrix):
            if self.n != other.m or self.m != other.n:
                sys.exit("Matrix dimensions do not match. Aborting!")

            return Matrix(self.n, self.n, [sum(map(lambda x : x[0]*x[1], zip(self.get_row(k/self.n), other.get_col(k)))) for k in range(0, self.n*self.n)])

        else:
            sys.exit("Cannot multiply matrix and object of type " + str(type(other)))
   

            
    def __rmul__(self, other):
        if isinstance(other, (int, float, long)):
            return Matrix(self.n, self.m, [other*x for x in self.values])

        elif isinstance(other, Matrix):
            if self.n != other.m or self.m != other.n:
                sys.exit("Matrix dimensions do not match. Aborting!")

            return Matrix(self.m, self.m, [sum(map(lambda x : x[0]*x[1], zip(other.get_row(k/other.n), self.get_col(k)))) for k in range(0, self.m*self.m)])

        else:
            sys.exit("Cannot multiply matrix and object of type " + str(type(other)))



    def transpose(self):
        return Matrix(self.m, self.n, [self.values[(k%self.n)*self.m + (k/self.n)] for k in range(0, self.n*self.m)])



    def print_matrix(self):
        print self.__str__()
        #print "\n\n",
        #print "["

        #for i in range(0, self.n):
        #    for j in range(0, self.m):
        #        print '{:>6,.2f}'.format(self.values[self.m*i + j]),
        #        print ',',
        #    print "\n",

        #print "]"



    def get_row(self, row):
        row = row % self.n
        return self.values[row*self.m:(row+1)*self.m]



    def get_col(self, col):
        col = col % self.m
        values = []
        for i in range(0, self.n):
            values.append(self.values[i*self.m + col])
        return values



    def row_mult(self, row_num, const):
        for i in range(row_num*self.m, (row_num+1)*self.m):
            self.values[i] = const*self.values[i]



    def row_swap(self, row_num_alpha, row_num_beta):
	for i in range(self.m):
	    offset_alpha = row_num_alpha*self.m + i
	    offset_beta = row_num_beta*self.m + i
	    temp = self.values[offset_alpha]
	    self.values[offset_alpha] = self.values[offset_beta]
	    self.values[offset_beta] = temp



    # Linear combination is stored in row_num_alpha.
    def row_comb(self, row_num_alpha, const_alpha, row_num_beta, const_beta):
	for i in range(self.m):
	    offset_alpha = row_num_alpha*self.m + i
	    offset_beta = row_num_beta*self.m + i
	    self.values[offset_alpha] = const_alpha*self.values[offset_alpha] + const_beta*self.values[offset_beta]



    def eliminate(self):
	for i in range(0, self.n-1):
	    for j in range(i+1, self.n):
		if self.values[i*self.m + i] == 0:
		    pass
		self.row_comb(j, 1, i, -1 * float(self.values[j*self.m + i])/float(self.values[i*self.m + i]))



class NullMatrix(Matrix):

    def __init__(self, dim):
        values = [0 for x in range(0, pow(dim, 2))]

        print values

        Matrix.__init__(self, dim, dim, values)



class IdentityMatrix(Matrix):

    def __init__(self, dim):
        values = []

        for i in range(0, dim):
            for j in range(0, dim):
                if i == j:
                    values.append(1)
                else:
                    values.append(0)

        Matrix.__init__(self, dim, dim, values)



# Test script.
#mat = Matrix(2, 2, [1, 0, 0, 1])
#mat.print_matrix()

#nullmat = NullMatrix(4)
#print nullmat

#idmat = IdentityMatrix(5)
#print idmat

#mat = Matrix(3, 3, [1, 2, 3, 2, 1, 3, 3, 2, 1])
#print mat

#mat.row_mult(1, 2)
#print mat
#mat.row_mult(1, 1.0/2)
#mat.print_matrix()

#mat.row_swap(1, 2)
#print mat

#mat.row_comb(0, 2, 1, 1)
#print mat

#mat.eliminate()
#print mat

#mat = Matrix(3, 3, [1, 2, 3, 2, 1, 3, 3, 2, 1])
#print mat
#mat = mat * 3.7
#mat = 3.7 * mat
#print mat

#mat1 = Matrix(3, 2, [1, 2, 3, 2, 1, 3])
#mat2 = Matrix(3, 2, [3, 2, 1, 3, 3, 2])
#mat3 = mat1 + mat2
#print mat1
#print "\n+\n",
#print mat2
#print "\n=\n",
#print mat3

#mat2 = Matrix(2, 3, [3, 2, 1, 3, 3, 2])
#print mat2
#print mat2[1][1]
#print mat2.transpose()

#print mat1.get_row(0)
#print mat2.get_col(0)
#print sum(map(lambda x : x[0]*x[1], zip( mat1.get_row(2), mat2.get_col(0) )))

#mat3 = mat1 * mat2
#print mat1
#print "\n*\n",
#print mat2
#print "\n=\n",
#print mat3

#mat3 = mat2 * mat1
#print mat2
#print "\n*\n",
#print mat1
#print "\n=\n",
#print mat3
