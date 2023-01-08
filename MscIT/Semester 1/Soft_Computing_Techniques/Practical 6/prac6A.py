# 6A. Kohonen self organizing map.
from minisom import MiniSom
import numpy as np
import matplotlib.pyplot as plt

colors = [
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 1.0],
    [0.0, 0.0, 0.5],
    [0.125, 0.529, 1.0],
    [0.33, 0.4, 0.67],
    [0.6, 0.5, 1.0],
    [0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 1.0],
    [1.0, 0.0, 1.0],
    [1.0, 1.0, 0.0],
    [1.0, 1.0, 1.0],
    [0.33, 0.33, 0.33],
    [0.5, 0.5, 0.5],
    [0.66, 0.66, 0.66],
]

color_names = [
    "black",
    "blue",
    "darkblue",
    "skyblue",
    "greyblue",
    "lilac",
    "green",
    "red",
    "cyan",
    "violet",
    "yellow",
    "white",
    "darkgrey",
    "mediumgrey",
    "lightgrey",
]

som = MiniSom(30, 30, 3, sigma=3.0, learning_rate=2.5, neighborhood_function="gaussian")

plt.imshow(abs(som.get_weights()), interpolation="none")
som = MiniSom(30, 30, 3, sigma=8.0, learning_rate=0.5, neighborhood_function="bubble")

som.train_random(colors, 500, verbose=True)
plt.imshow(abs(som.get_weights()), interpolation="none")

