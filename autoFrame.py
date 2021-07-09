from PIL import Image, ImageDraw, ImageFont, ImageFilter

image = Image.open("cox's_bazar.jpg")
font = ImageFont.truetype("arial.ttf", 28, encoding="unic")
draw = ImageDraw.Draw(image)
draw.text(xy=(50, 50), text="shishir", fill=(255, 69, 0), font=font)
# image.show()


# importing modlue
from pandas import *

# reading CSV file
data = read_csv("./frameCSV.csv")

# converting column data to list
photo = data["Upload Your decent Photo"].tolist()
name = data["Name"].tolist()
student_id = data["Student ID"].tolist()


# printing list data
# print("Photo:", photo)


# import requests

# x = requests.get(
#     "https://drive.google.com/file/d/1PfKwLWcJtDK43BruXi7qioDApQX9s53B/view"
# )
# print(x.status_code)
# x.show()

# import requests
# from io import BytesIO

# url = "https://drive.google.com/file/d/1PfKwLWcJtDK43BruXi7qioDApQX9s53B/view"
# response = requests.get(url)
# img = Image.open(BytesIO(response.content))
# img.show()

from PIL import Image
import io
import requests
import matplotlib.pyplot as plt

# find id

for j in name:
    image = Image.open('./template.png')
    font = ImageFont.truetype("arial.ttf",60, encoding="unic")
    draw = ImageDraw.Draw(image)
    draw.text(xy=(200, 800), text="{0}".format(j), fill=(255, 69, 0), font=font)
    image.show()

for i in photo:
    id = i.split("=")[1]
    print("Id:", id)
    url = "https://drive.google.com/uc?export=view&id={0}".format(id)
    print(url)

    response = requests.get(url, stream=True)

    img = Image.open(response.raw)

    newsize = (600, 600)
    img = img.resize(newsize)

    mask_im = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask_im)
    draw.ellipse((0, 0, 600, 600), fill=255)

    tamplate = Image.open("./template.png")

    tamplate.paste(img, (200, 150), mask_im)
    # tamplate.show()
    # tamplate.close()

    # back_im = tamplate.copy()
    # back_im.paste(img)
    # back_im.save("./abx.jpg", quality=95)

    # plt.imshow(img)
    # plt.show()
    # plt.close()


