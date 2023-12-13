from PIL import ImageDraw, Image, ImageFilter, ImageChops

img = Image.open('Png.png')
background = Image.open('back.jpg')
background = background.crop((0, 0, background.width, background.height)).resize((img.width, img. height)).transpose(Image.FLIP_LEFT_RIGHT)
r, g, b, a = img.split()


mask_temp = g.point(lambda x: (x > 0 and x < 90 ) and 255)
mask = ImageChops.invert(mask_temp)
new_img = Image.composite(img, background, mask)
new_img.show()
new_img.convert('L')
new_img = new_img.filter(ImageFilter.GaussianBlur(5))
new_img.show()