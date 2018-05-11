#For plotting the images
from matplotlib import pyplot as plt
import numpy as np
from som__ import SOM

#Training inputs for RGBcolors
colors = np.array(
     [[0., 0., 0.],
      [0., 0., 1.],
      [0., 0., 0.5],
      [0.125, 0.529, 1.0],
      [0.33, 0.4, 0.67],
      [0.6, 0.5, 1.0],
      [0., 1., 0.],
      [1., 0., 0.],
      [0., 1., 1.],
      [1., 0., 1.],
      [1., 1., 0.],
      [1., 1., 1.],
      [.33, .33, .33],
      [.5, .5, .5],
      [.66, .66, .66]])


som = SOM(50, 50, 3, n_iterations=1000, sigma=20, sample_epoches=[1, 20, 40, 100, 1000])
som.train(colors)

#Get output grid
image_grids = som.get_centroids()

#Map colours to their closest neurons
# mapped = som.map_vects(colors)

#Plot

for i,grid in enumerate(image_grids):
  plt.imshow(grid)
  plt.title('Color SOM')

  plt.savefig("data/" + str(i) + ".png")

  plt.clf()


