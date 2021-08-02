import numpy as np
cimport numpy as np

def update(np.ndarray[np.int_t, ndim=2] grid, int N):
    cdef np.int_t[:, :] new_grid = grid.copy()
    cdef int i
    cdef int j
    cdef int total
    cdef int ON = 255
    cdef int OFF = 0
    for i from 0<= i < N:
        for j from 0<= j <N:
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)

            # apply Conway's rules
            if grid[i, j]  == ON:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = OFF
            else:
                if total == 3:
                    new_grid[i, j] = ON

    # update data
    grid[:] = new_grid[:]
    return grid


