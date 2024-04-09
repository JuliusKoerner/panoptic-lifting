import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.colors as mcolors
import copy


class visualizerForIds:
    def __init__(self, seed=1234):
        np.random.seed(seed)
        self.colors = [np.random.random(3) for i in range(0, 1000)]

        self.colors.insert(0, [1, 1, 1])
        self.colors.insert(0, [0, 0, 0])
        self.cmap = mcolors.ListedColormap(self.colors)

    def get_colors(self, ids):
        return self.cmap(ids)

    def visualize(self, anns, path=None, ax=None, title="", prompts=None):

        ids = copy.deepcopy(anns)
        ids[ids < 0] = 100
        if path is not None:
            plt.imshow(ids, cmap=self.cmap, vmin=0, vmax=len(self.colors) - 1)
            if prompts is not None:
                plt.scatter(
                    prompts[:, 0], prompts[:, 1], s=10, c="blue", marker="o", alpha=0.5
                )
                plt.title(title)
            plt.savefig(path)
            plt.clf()
            return
        if ax is None:
            im = plt.imshow(ids, cmap=self.cmap, vmin=0, vmax=len(self.colors) - 1)
            return im
        ax.set_title(title)
        im = ax.imshow(ids, cmap=self.cmap, vmin=0, vmax=len(self.colors) - 1)

        return ax, im

    def visualizer(self, anns, path, title="", prompts=None):
        # Create a 2D numpy array
        # plt.title(title)
        plt.figure(figsize=(10, 10))
        plt.imshow(anns, cmap=self.cmap, vmin=0, vmax=len(self.colors) - 1)
        if prompts is not None:
            plt.scatter(prompts[0, :], prompts[1, :], s=100, c="red", marker="o")
        plt.savefig(path)

        plt.show()
