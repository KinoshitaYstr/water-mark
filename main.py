import numpy as np
from PIL import Image
from DivisionBit import DivisionBit
from DivisionBit import BitImg

def main():
    base_size = 100
    img1 = Image.open("data/Lenna.png").convert("L").resize((base_size*4,base_size*4))
    img_array1 = np.asanyarray(img1)
    img2 = Image.open("data/idol_fan_penlight_men.png").convert("L").resize((base_size, base_size))
    img_array2 = np.asanyarray(img2)
    BitImg1 = DivisionBit(img_array1)
    BitImg1.deivide()
    BitImg2 = DivisionBit(img_array2)
    BitImg2.deivide()
    BitImg2.set_flat()
    BitImg1.change(BitImg2,0)
    BitImg1.save("result/test.png")
    BitImg1.show()
    img_r = Image.open("result/test.png").convert("L")
    img_r_array = np.asarray(img_r)
#    img_r.show()
    R = DivisionBit(img_r_array)
    R.deivide()
    R.show_flat_all()
    BI = BitImg(R.flat[7])
    BI.create_img(base_size,base_size)

def create_data(fname):
    img2 = Image.open("data/"+fname).convert("L")
    img_array2 = np.asanyarray(img2)
    img_array2 = np.where(img_array2 == 0,100,img_array2)
    Image.fromarray(img_array2).convert("RGB").save("data/"+fname)
    
if __name__ == "__main__":
    main()
