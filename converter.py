from PIL import Image, ImageFont, ImageDraw
import numpy as np
np.set_printoptions(threshold=np.inf)


#inputs
imagePath = "image.png"
size = (50,50)
fontPath = "C:/Windows/Fonts/courbd.ttf"
fontSize = 30

im = Image.open(imagePath)
im = im.resize(size)
nim = im.convert('1')

dataArray = ~np.array(nim)
dataArray = dataArray.astype(int)
dataArray = dataArray.astype(str)

onesZeros = "\n".join(" ".join(row) for row in dataArray)
print('STRING')
print(onesZeros)



# create an image
out = Image.new("RGB", (1080, 1080), (255, 255, 255))

# get a font
fnt = ImageFont.truetype(fontPath, fontSize)
# get a drawing context
d = ImageDraw.Draw(out)

# draw multiline text
d.multiline_text((10, 10), onesZeros, font=fnt, fill=(0, 0, 0))

out.show()