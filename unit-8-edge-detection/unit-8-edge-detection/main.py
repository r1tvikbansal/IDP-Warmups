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
    backwhite = np.dot(duck[..., :3], [0.2989, 0.5870, 0.1140])
    for h in range(1, 3):
        for w in range(1, 3):
            sliced = backwhite[h - 1: h + 2, w - 1: w + 2]
            new = sliced * kernel
            print(new)
            print('----')
            for row in new:
                for pix in row:
                    if pix > 127:
                        new[row, pix] = 255
                    else:
                        new[row, pix] = 0
            print(new)
            print('----------------------')
            # print('--------------------------------------')
            # for kc in range(3):
            #     for kr in range(3):
            #         print(sliced[kc, kr], 'on', kernel[kc, kr])
            #         sliced[kc, kr] *= kernel[kc, kr]
            #         print(sliced[kc, kr])
    # Normalize the image
    
    return duck


def main():
    duck = imageio.imread("duck.jpg")
    duck = edge_detect(duck)
    # plt.imshow(duck)
    # plt.savefig("edge_detect.png")


if __name__ == "__main__":
    main()
