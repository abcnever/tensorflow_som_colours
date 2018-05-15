from matplotlib import pyplot as plt
import numpy as np
from app.models import SOM
from pathlib import Path

# threaded function to handle model training
def process_som_model(colors):
  sample_epoches = [1, 20, 40, 100, 1000]

  som = SOM(50, 50, 3, n_iterations=1000, sample_epoches=sample_epoches)
  som.train(colors)

  image_grids = som.get_centroids()

  for i, grid in enumerate(image_grids):
    plt.imshow(grid)
    plt.title('Color SOM at k=' + str(sample_epoches[i]) + ' epoch(es)')

    plt.savefig("app/static/data/" + str(i) + ".png")

    plt.clf()

  print('Figures saved.')
