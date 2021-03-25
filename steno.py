from PIL import Image as im
import sys
import os
import re

def Encode(image, text):
    img = OpenImage(image)
    img = Normalize(img)
    bin_text = TextToBin(text)
    new_img = Embed(img, bin_text)
    name = GetName()
    new_img.save(name, "PNG")
    return name

def Decode(image):
    img = OpenImage(image)
    bin_text = Extract(img)
    text = BinToText(bin_text)
    return text

def OpenImage(image):
    try:
        image = im.open(image)
        image = image.convert("RGB")
    except:
        print("Can't open the image")
        sys.exit(1)
    return image

def Normalize(img):
    mask = 254
    pixels = list(img.getdata())
    i = 0
    for pixel in pixels:
        new_pixel = 0
        if type(pixel) == int:
            new_pixel = pixel & mask
        elif type(pixel) == tuple:
            temp = ()
            for byte in pixel:
                temp += (byte & mask, )
            new_pixel = temp
        pixels[i] = new_pixel
        i += 1
    new_img = im.new(img.mode, img.size)
    new_img.putdata(pixels)
    return new_img

def TextToBin(text):
    result = ""
    byte = bytes(text, "ascii")
    for letter in byte:
        binary = bin(letter)[2:]
        result += "0"*(8 - len(binary)) + binary
    return result

def Embed(img, bin_text):
    i_text = 0
    i_img = 0
    pixels = list(img.getdata())
    while i_text < len(bin_text):
        pixel = pixels[i_img]
        new_pixel = 0
        if type(pixel) == int:
            new_pixel = pixel | int(bin_text[i_text])
            i_text += 1
        elif type(pixel) == tuple:
            temp = ()
            for byte in pixel:
                if i_text >= len(bin_text):
                    temp += (byte, )
                else:
                    temp += (byte | int(bin_text[i_text]), )
                i_text += 1
            new_pixel = temp
        pixels[i_img] = new_pixel
        i_img += 1
    new_img = im.new(img.mode, img.size)
    new_img.putdata(pixels)
    return new_img

def GetName():
    format = "png"
    base_name = "result"
    name = base_name + "." + format
    i = 1
    while os.path.isfile(name):
        name = base_name + str(i) + "." + format
        i += 1
    return name


def Extract(img):
    mask = 1
    pixels = list(img.getdata())
    result = ""
    for pixel in pixels:
        data = ""
        if type(pixel) == int:
            data = str(pixel & mask)
        elif type(pixel) == tuple:
            temp = ""
            for byte in pixel:
                temp += str(byte & mask)
            data = temp
        result += data
    return result

def BinToText(bin_text):
    text = ''.join(chr(int(bin_text[i*8:i*8+8], 2)) for i in range(len(bin_text)//8))
    text = re.sub("\0", "", text)
    return text

if __name__ == "__main__":
    uinput = input("encode or decode [e, d]?")
    if uinput.lower() == "e":
        image = input("image path : ")
        text = input("message to encode : ")
        file = Encode(image, text)
        print("File Output {}".format(file))
    elif uinput.lower() == "d":
        image = input("image path : ")
        print(Decode(image))
        
