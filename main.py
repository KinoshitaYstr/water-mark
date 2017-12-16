import numpy as np
from PIL import Image
from DivisionBit import DivisionBit

def main():
    img = Image.open("data/Lenna.png").convert("L")
    img_array1 = np.asarray(img)
    DB1 = DivisionBit(img_array1)
    DB1.deivide()
    DB1.match()
    DB1.set_flat()

if __name__ == "__main__":
    main()
