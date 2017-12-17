import numpy as np
from PIL import Image
from DivisionBit import DivisionBit
from DivisionBit import BitImg

class SimpleWaterMarkSet:
    def __init__(self,fname,base_fname,img_size_x,img_size_y):
        img = Image.open(fname).convert("L").resize((img_size_x, img_size_y))
        base = Image.open(base_fname).convert("L").resize((img_size_x*4, img_size_y*4))
        self.img_array = np.asarray(img)
        self.base_array = np.asarray(base)
        self.img_bit = DivisionBit(self.img_array)
        self.base_bit = DivisionBit(self.base_array)
    def calc(self,fname):
        self.img_bit.deivide()
        self.img_bit.set_flat()
        self.base_bit.deivide()
        self.base_bit.change(self.img_bit,0)
        self.base_bit.flat2array()
        self.base_bit.save(fname)

class SimpleWaterMarkReset:
    def __init__(self,fname):
        img = Image.open(fname).convert("L")
        self.img_array = np.asarray(img)
        d = DivisionBit(self.img_array)
        d.deivide()
        self.img_bit = BitImg(d.flat[0])
    def calc(self,fname):
        (y,x) = self.img_array.shape
        self.img_bit.create_img(int(y/4),int(x/4))
        self.img_bit.save(fname)
    
