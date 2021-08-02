import numpy as np
import matplotlib.pyplot as plt
# import cv2
import time

# matrix dimension - N*N
N = 400

# for representation as pixels in the resulting image
ON = 255
OFF = 0

def update(grid):
    ''' Function to run The Game of life, generating the next state from the current state'''
    # to store the new state
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            # implementing the toroidal boundary conditions
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)

            # applying Conway's rules
            if grid[i, j]  == ON:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = OFF
            else:
                if total == 3:
                    new_grid[i, j] = ON

    # return the new state
    grid[:] = new_grid[:]
    return grid


def main():

    # grid, defined random producing more OFF than ON
    grid = np.random.choice([ON, OFF], N*N, p=[0.2, 0.8]).reshape(N, N)

    # create OpenCV video writer
    # video = cv2.VideoWriter('python.avi', cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), 1, (640, 480))

    # interactive plot
    plt.ion()
    fig, ax = plt.subplots()
    fig.suptitle('This is the python version', fontsize=16)
    # set a frame
    img = ax.imshow(grid, interpolation='nearest')
    # run for 10 seconds
    t_end = time.time() + 10
    while time.time() < t_end:
        # get the new state
        new_grid = update(grid)
        # update the frame
        img.set_data(new_grid)
        # plot the frame
        fig.canvas.draw()

        # frames for video
        # mat = np.array(fig.canvas.renderer._renderer)
        # mat = cv2.cvtColor(mat, cv2.COLOR_RGB2BGR)

        # write frame to video
        # video.write(mat)

        fig.canvas.flush_events()

    # close video writer
    # cv2.destroyAllWindows()
    # video.release()

# call main
if __name__ == '__main__':
    main()