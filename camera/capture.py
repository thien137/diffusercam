from PIL import Image, ImageOps
from io import BytesIO
import requests

def capture(server):
    x = requests.get(f'http://{server}/stream/d')
    im = Image.open(BytesIO(x.content))

    return im

if __name__ == "__main__":
    server = '192.168.0.23'
    im = capture(server)
    im = ImageOps.grayscale(im)
    
    while (True):
        try:
            im = im.save(input("Enter location of image file: "))
            break
        except:
            print("Error: Invalid File Location/Unable to Save Image")
            continue