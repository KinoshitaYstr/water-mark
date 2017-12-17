import numpy as np
from PIL import Image
from DivisionBit import DivisionBit
from DivisionBit import BitImg
from WaterMark import SimpleWaterMarkSet
from WaterMark import SimpleWaterMarkReset

def main_test():
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
    #BitImg1.reset_flat()
    BitImg1.flat2array()
    BitImg1.save("result/test.png")
    #BitImg1.deivide()
    #BitImg1.show_flat(0)
    #BitImg1.show()
    img_r = Image.open("result/test.png").convert("L")
    img_r.show()
    img_r_array = np.asarray(img_r)
#    img_r.show()
    R = DivisionBit(img_r_array)
    R.deivide()
    #R.show_flat(0)
    #R.show_flat_all()
    BI = BitImg(R.flat[0])
    BI.create_img(base_size,base_size)

def create_data(fname):
    img2 = Image.open("data/"+fname).convert("L")
    img_array2 = np.asanyarray(img2)
    img_array2 = np.where(img_array2 == 0,100,img_array2)
    Image.fromarray(img_array2).convert("RGB").save("data/"+fname)

def main():
    print("電子透かし -> 1,解除 -> 2")
    mode = input("モード選択 : ")
    if mode == "1":
        fname = "data/"+input("挿入画像名入力 : ")
        base = "data/" + input("挿入先画像名入力 : ")
        save_fname = "result/"+input("保存画像名入力 : ")
        sws = SimpleWaterMarkSet(fname,base,100,100)
        sws.calc(save_fname)
    else:
        fname = "data/"+input("画像名入力 : ")
        save_fname = "result/" + input("保存画像名入力 : ")
        swr = SimpleWaterMarkReset(fname)
        swr.calc(save_fname)
    

if __name__ == "__main__":
    #main_test()
    main()
