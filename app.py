import struct
import sys

def readUnsignedInt(file):
    """Reads 32-bits of unsigned integer data from a stream"""
    return struct.unpack("<I", file.read(4))[0]

def parseBMP(args):
    """Parses a BMP file using the standard BMP format"""
    try:
        imgPath = args[1]
        file = open(imgPath, "rb")
    except IndexError:
        print("No argument specified for the image path")
        return
    except FileNotFoundError:
        print("Failed to open specified image at", imgPath)
        return
    
    file.seek(2)
    fileSize = readUnsignedInt(file)
    file.seek(10)
    dataOffset = readUnsignedInt(file)
    file.seek(14)
    imgSize = readUnsignedInt(file)
    file.seek(18)
    imgWidth = readUnsignedInt(file)
    file.seek(22)
    imgHeight = readUnsignedInt(file)
    file.seek(28)
    bbp = struct.unpack("<H", file.read(2))[0]
    print("The image '%s' has the following properties:" % imgPath)
    print("Width: %d\nHeight: %d\nTotal size in bytes: %d\nBits per pixel: %d" % (imgWidth, imgHeight, imgSize, bbp))

if __name__ == "__main__":
    parseBMP(sys.argv)