import numpy as np
from PIL import Image
from DivisionBit import DivisionBit
from DivisionBit import BitImg
from WaterMark import SimpleWaterMarkSet
from WaterMark import SimpleWaterMarkReset

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
    main()
