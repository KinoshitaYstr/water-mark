import numpy as np
from PIL import Image
from DivisionBit import DivisionBit

def main():
    img = Image.open("data/Lenna.png").convert("L").resize((50,50))
    img_array1 = np.asarray(img)
    DB1 = DivisionBit(img_array1)
    DB1.deivide()
    DB1.match()
    DB1.set_flat()
    DB1.reset_flat()
    DB1.match()
    DB1.save("result/flat1.png")
if __name__ == "__main__":
    main()
