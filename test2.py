import numpy as np
from scipy.sparse import csr_matrix


num_add_user = 5
num_user = 1

sparse_matrix_add_user = csr_matrix((num_add_user, num_user), dtype=np.int32)

sparse_matrix_add_user[0] = 5
sparse_matrix_add_user[1] = 2


print("Sparse Matrix add user:")
print(sparse_matrix_add_user.toarray())

