import json
from PIL import Image, ImageDraw, ImageFilter,ImageFont
import requests
from io import BytesIO


  
# Opening JSON file
f = open('./frameJSON.json',encoding="utf8")
  
# returns JSON object as  a dictionary

data = json.load(f)
  
# Iterating through the json list

for i in data:
    print(i['Name'])
    print(i['Student ID'])

    #get the photo
    id = i['Upload Your decent Photo'].split("=")[1]
    print("Id:", id)
    url = "https://drive.google.com/uc?export=view&id={0}".format(id)
    print(url)

    response = requests.get(url, stream=True)
    #resize the photo and set it in the tamplate
    img = Image.open(BytesIO(response.content))
    img.save("{0}.png".format(i['Student ID']), format="png")
f.close()
