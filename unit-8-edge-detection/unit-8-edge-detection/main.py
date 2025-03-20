import imageio.v2 as imageio
import numpy as np
import matplotlib.pyplot as plt

def edge_detect(image):
    kernel = np.array([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ])
    
    grayscale = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    
    height, width = grayscale.shape
    
    edge_image = np.zeros_like(grayscale)
    
    for h in range(1, height - 1):
        for w in range(1, width - 1):
            region = grayscale[h - 1:h + 2, w - 1:w + 2]
            edge_value = np.sum(region * kernel)
            edge_image[h, w] = 0 if edge_value > 127 else 255

    return edge_image

def main():
    image = imageio.imread("/workspaces/IDP-Warmups/unit-8-edge-detection/unit-8-edge-detection/duck.jpg")
    
    edge_image = edge_detect(image)
    
    plt.imshow(edge_image, cmap='gray')
    plt.title("Edge Detected Image")
    plt.grid(True)
    plt.show()
    
    plt.imsave("edge_detected_output.png", edge_image, cmap='gray')

if __name__ == "__main__":
    main()
