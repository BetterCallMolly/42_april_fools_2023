from PIL import Image
import PIL.ImageOps    

image = Image.open("42.png").convert("RGB")

# Invert colors
inverted_image = PIL.ImageOps.invert(image)

# Turn full black pixels to green
pixels = inverted_image.load()
for i in range(inverted_image.size[0]):
	for j in range(inverted_image.size[1]):
		if pixels[i, j] == (0, 0, 0):
			pixels[i, j] = (0, 255, 0)

inverted_image.save('new_name.png')