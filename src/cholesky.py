import math
from matrix import Matrix, NullMatrix, IdentityMatrix

class Cholesky:

    def __init__(self):
        pass



    def llt_decomp(self, matrix):
        l = self.r_llt_decomp(0, matrix, IdentityMatrix(matrix.n))
        lt = l.transpose()
        return l, lt

    def r_llt_decomp(self, i, a_mat, l_mat):
        if i == a_mat.n:
            return l_mat

        # Get the scalar a_ii.
        a_sca = a_mat[i, i]
        # Get the vector b_i.
        b_vec = [0] * a_mat.n
        b_vec[i+1:a_mat.n] = a_mat.get_col(i)[i+1:a_mat.n]
        #print b_vec


        # Begin computing L_i+1.

        # Set up an identity matrix for the new term of L.
        m_mat = IdentityMatrix(a_mat.n)

        # Set M[i, i] to sqrt(a[i, i]).
        #print "a_sca:" + str(a_sca)
        m_mat[i, i] = math.sqrt(a_sca)

        # Set the term to a[i+1, i]/sqrt(a[i, i]).
        for k in range(i+1, a_mat.n):
            m_mat[k, i] = b_vec[k]/m_mat[i, i]

        # End computing L_i+1.


        # Set up the vectors b_i and b_i^t to compute the outer product op_mat.
        op_mat = Matrix(len(b_vec), 1, b_vec) * Matrix(1, len(b_vec), b_vec)

        b_mat = NullMatrix(a_mat.n)
        for p in range(i+1, a_mat.n):
            for q in range(i+1, a_mat.m):
                b_mat[p, q] = a_mat[p, q]

        c_mat = b_mat - (1/a_sca)*op_mat

        for k in range(0, i):
            c_mat[k, k] = 1


        return self.r_llt_decomp(i+1, c_mat, l_mat*m_mat)



    def ldlt_decomp(self, matrix):
        l = self.llt_decomp(matrix)[0]
        d = IdentityMatrix(matrix.n)
        
        for i in range(0, d.n):
            d[i, i] = l[i, i]
            for j in range(i, d.n):
                l[j, i] = l[j, i]/d[i, i]
            d[i, i] = d[i, i] ** 2

        lt = l.transpose()

        return l, d, lt



matrix = Matrix(3, 3, [4, 12, -16, 12, 37, -43, -16, -43, 98])
print matrix

decomp = Cholesky()

llt = decomp.llt_decomp(matrix)
print llt[0]
print llt[1]


ldlt = decomp.ldlt_decomp(matrix)
print ldlt[0]
print ldlt[1]
print ldlt[2]
