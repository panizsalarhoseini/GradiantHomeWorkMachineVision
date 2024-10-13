from PIL import Image
import numpy as np

def create_gradient_image(width, height, point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    gradient = np.zeros((height, width, 3), dtype=np.uint8)
    
    for x in range(width):
        for y in range(height):
            t = ((x - x1) * (x2 - x1) + (y - y1) * (y2 - y1)) / float((x2 - x1)**2 + (y2 - y1)**2)
            t = max(0, min(1, t))
            color = int(t * 255)
            gradient[y, x] = [color, color, color]
    image = Image.fromarray(gradient)
    return image
width, height = 256, 256
point1 = (0, 0)
point2 = (0, 255)
gradient_image = create_gradient_image(width, height, point1, point2)
gradient_image.save("gradient_image.png")
print("Gradient image created and saved as gradient_image.png")
gradient_image.show()
