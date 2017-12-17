import numpy as np
from PIL import Image
from DivisionBit import DivisionBit
from DivisionBit import BitImg

def main():
    """
    img1 = Image.open("data/Lenna.png").convert("L").resize((100,50))
    img1.show()
    img_array1 = np.asanyarray(img1)
    b = DivisionBit(img_array1)
    b.deivide()
    b.set_flat()
    """

    base_size = 50
    img1 = Image.open("data/Lenna.png").convert("L").resize((base_size*4,base_size*4))
    img_array1 = np.asanyarray(img1)
    img2 = Image.open("data/idol_fan_penlight_men.png").convert("L").resize((base_size,base_size))
    img_array2 = np.asanyarray(img2)
    print(img_array2.shape)
    BitImg1 = DivisionBit(img_array1)
    BitImg1.deivide()
    BitImg2 = DivisionBit(img_array2)
    BitImg2.deivide()
    BitImg2.set_flat()
    BitImg1.change(BitImg2,0)
    BitImg1.save("result/test.png")

    img_r = Image.open("result/test.png").convert("L")
    img_r_array = np.asarray(img_r)
    r = DivisionBit(img_r_array)
    r.deivide()
    #r.show_flat_all()

    BI = BitImg(BitImg1.flat[0])
    BI.create_img(50,50)
    
if __name__ == "__main__":
    main()
