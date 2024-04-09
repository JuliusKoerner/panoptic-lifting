import glob
from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt
from vis import visualizerForIds


def make_gif(frame_folder):
    visualizerForId = visualizerForIds()
    files = sorted(glob.glob(f"{frame_folder}/*.png"))
    frames = []
    for file in files:
        ids = np.array(Image.open(file))
        colors = visualizerForId.get_colors(ids) * 255
        im = Image.fromarray(colors.astype(np.uint8))
        frames.append(im)
    frame_one = frames[0]
    frame_one.save(
        os.path.join(frame_folder, "gif.gif"),
        format="GIF",
        append_images=frames,
        save_all=True,
        duration=100,
        loop=0,
    )


def make_gif_from_array(semantic_frames, store, max_frame=-1, duration=100):
    frames = []
    for frame in semantic_frames[:max_frame]:
        im = Image.fromarray((frame * 255).astype(np.uint8))
        frames.append(im)
    frame_one = frames[0]
    frame_one.save(
        store,
        format="GIF",
        append_images=frames,
        save_all=True,
        duration=duration,
        loop=0,
    )

    # Rest of the code...


if __name__ == "__main__":
    make_gif("/home/koerner/Project/nice-slam/Datasets/Replica/room0/segmentation")
