import math
import matrix

class Cholesky:

    def __init__(self):
        pass



    def llt_decomp(self, matrix):
        return r_llt_decomp(1, matrix, IdentityMatrix(matrix.n))

    def r_llt_decomp(self, i, a_mat, l_mat):
        if i == a_mat.n:
            return l_mat

        # Get the vector b_i.
        b_vec = a_mat.get_col(i) #[i+1:a_mat.n]

        # Begin computing L_i+1.
        # Set up an identity matrix for the new term of L.
        m_mat = IdentityMatrix(a_mat.n)
        # Set M[i, i] to sqrt(a[i, i]).
        m_mat[i, i] = math.sqrt(a_mat[i, i])
        # Set the term to a[i+1, i]/sqrt(a[i, i]).
        for k in range(0, a_math.n):
            m_mat[i+1, k] = b_vec[k]/m_mat[i, i]
        # End computing L_i+1.
       
        # Set up the vectors b_i and b_i^t to compute the outer product op_mat.
        b_mat = Matrix(1, len(b_vec), b_vec)
        bt_mat = Matrix(len(b_vec), 1, b_vec)
        op_mat = b_mat * bt_mat

        # Generate 

        return r_llt_decomp(i+1, a_mat, l_mat)



    def ldlt_decomp(self, matrix):
        pass



matrix = NullMatrix()
decomp = Cholesky()

llt = decomp.llt_decomp(matrix)
print llt


ldlt = decomp.ldlt_decomp(matrix)
print ldlt
