from PIL import Image, ImageDraw, ImageFilter

im1 = Image.open("./template.png")
im2 = Image.open("./template.png")

newsize = (600, 600)
im2 = im2.resize(newsize)


mask_im = Image.new("L", im2.size, 0)
draw = ImageDraw.Draw(mask_im)
draw.ellipse((0,0,600, 600), fill=255)

mask_im = mask_im.filter(ImageFilter.GaussianBlur(10))

# mask_im.show()

back_im = im1.copy()
back_im.paste(im2, (100, 100), mask_im)
back_im.show()

print(draw.textsize(shishir))
