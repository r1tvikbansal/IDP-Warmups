import imageio
import matplotlib.pyplot as plt


# Write your function here!
def duckie_hat(image):
    image2 = image.copy()
    image2[20:75, 85:135] = [0, 255, 0]
    image2[75:90, 60:160] = [0, 255, 0]
    return image2


def main():
    duck = imageio.imread("duck.jpg")
    duck = duckie_hat(duck)
    plt.imshow(duck)
    plt.savefig("duckie_hat.png")


if __name__ == "__main__":
    main()
