from PIL import Image 
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)

image = Image.open('images/scenery.jpg')

# open
image.show()

# # resize
# resized_image = image.resize((round(image.width/2), round(image.height/2)))
# resized_image.show()

# # filter
# blurred_image = image.filter(BLUR)
# blurred_image.show()

# # save
# blurred_image.save('images/ImageFilter_blur.png')
