import imageio
import matplotlib.pyplot as plt
import numpy as np


# Write your function here!
def edge_detect(duck):
    # Define the kernel
    kernel = np.zeros((3, 3), dtype=np.int64) - 1
    kernel[1, 1] = 8
    print(kernel)
    print('adsfadsfadfadfa')
    # Apply the kernel
    height, width, color = duck.shape
    for h in range(1, 3):
        for w in range(1, 3):
            sliced = duck[h - 1: h + 2, w - 1: w + 2, :]    
            # print(sliced)
            # print('--------------------------------------')
            for kc in range(3):
                for kr in range(3):
                    print(sliced[kc, kr], 'on', kernel[kc, kr])
                    sliced[kc, kr] *= kernel[kc, kr]
                    print(sliced[kc, kr])
    # Normalize the image
    
    return duck


def main():
    duck = imageio.imread("duck.jpg")
    duck = edge_detect(duck)
    # plt.imshow(duck)
    # plt.savefig("edge_detect.png")


if __name__ == "__main__":
    main()
