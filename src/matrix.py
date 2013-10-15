class Matrix:

    def __init__(self, n, m=None, values=[]):
        if m == None:
            m = n

        self.n = n
        self.m = m

        values = map(lambda x : int(x), values)
        if len(values) == self.n*self.m:
            self.values = values[0:self.m*self.n-1]



    def print_matrix(self):
        print "\n\n[\n",

    	for i in range(self.n):
            print "\t",

            for j in range(self.m):
                print str(self.values[i*self.m + j]) + ",\t",

	    print "\n",

        print "]\n\n",



    def get_row(self, row):
        row = row % self.n
        return self.values[row*m:row*(self.m+1)-1]



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
        values = []
        
        for i in range(0, dim):
            for j in range(0, dim):
                values.append(0)

        print len(values)

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

nullmat = NullMatrix(4)
nullmat.print_matrix()

idmat = IdentityMatrix(5)
idmat.print_matrix()

mat = Matrix(3, 3, [1, 2, 3, 2, 1, 3, 3, 2, 1])
mat.print_matrix()

mat.row_mult(1, 2)
mat.print_matrix()
#mat.row_mult(1, 1.0/2)
#mat.print_matrix()

mat.row_swap(1, 2)
mat.print_matrix()

mat.row_comb(0, 2, 1, 1)
mat.print_matrix()

mat.eliminate()
mat.print_matrix()
