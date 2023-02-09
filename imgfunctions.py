from PIL import Image

def importpalette(palettefile):
    if not(palettefile.endswith(".png")):
        print("\u001b[33mWarning: Tt is recommended you use a png file as it is lossless\u001b[0m")
        ignore = input("Would you like to continue anyway? (y/N): ")
        if ignore.lower() in ["y", "yes"]:
            print("If this doesnt work try saving your palette as a png")
        else:
            return 1

    #if it fails to open
    try:
        im = Image.open(palettefile)
    except:
        print(f"\u001b[31mERR: Could not open file: \"{palettefile}\"\u001b[0m")
        return 1

    if im.mode == "RGBA":
        print("\u001b[33mWARN: this program can read transparent pixels as colours. please make sure to fill in all "
              "blank spaces\u001b[00m")


    #get the 8 colours
    pixels = im.load()
    width, height = im.size
    a = []
    for y in range(height):
        for x in range(width):
            pixelcolour = pixels[x, y]
            hex_value = "#{:02x}{:02x}{:02x}".format(pixelcolour[0], pixelcolour[1], pixelcolour[2])
            print(hex_value)
            if not (str(hex_value) in a):
                a.append(hex_value)
                if len(a) == 8:
                    return a

    print(f"\u001b[31mERROR: could not find 8 colours in palette image (found {len(a)})")
    return 1


def readimage(img, palette):
    if not(img.endswith(".png")): print("\u001b[33mWARN: non png type files may not be read correctly. It is "
                                            "reccommended to use a png file for this\u001b[00m")

    try:
        im = Image.open(img)
    except:
        print(f"\u001b[31mERR: Could not open file: \"{img}\"\u001b[0m")
        return 1

    if im.mode == "RGBA":
        print("\u001b[33mWARN: this program can read transparent pixels as colours. please make sure to fill in all "
              "blank spaces\u001b[00m")

    try:
        pixels = im.load()
    except:
        print("\u001b[31mERR: Could not open file\u001b[0m")
        return 1

    width, height = im.size
    instructions = []
    for y in range(height):
        for x in range(width):
            pixelcolour = pixels[x, y]
            hex_value = "#{:02x}{:02x}{:02x}".format(pixelcolour[0], pixelcolour[1], pixelcolour[2])
            for i in range(8):
                if hex_value == palette[i]:
                    instructions.append(i)

    return instructions

