import numpy as np
from PIL import Image

class DivisionBit:
    def __init__(self,array):
        self.array = array
        (self.y,self.x) = array.shape
        self.flat = []
    def deivide(self):
        flag = 0b1
        for i in range(8):
            self.flat.append(np.where(self.array & flag,1,0))
            flag = flag<<1
    def show_flat_all(self):
        for i in range(8):
            Image.fromarray(self.flat[i]*255).show()
    def show_flat(self,i):
        Image.fromarray(self.flat[i]*255).show()
    def match(self):
        self.array = np.zeros((self.y,self.x))
        flag = 0b1
        for i in range(8):
            self.array = self.array+self.flat[i]*flag
            flag = flag<<1
        Image.fromarray(self.array).show()
    def set_flat(self):
        flat = []
        for i in range(8):
            flat.append(self.flat[i].reshape(-1,))
        (size,) = flat[0].shape
        array = np.array([])
        for i in range(size):
            for j in range(8):
                array = np.append(array,flat[j][i])
        array = np.append(array,array)
        self.array = array.reshape((self.y * 4, self.x * 4))
        Image.fromarray(self.array * 255).show()
    def reset_flat(self):
        array = self.array.reshape(-1,)
        size, = array.shape
        size = int(size/2)
        array = array[:size]
        bit = [
            np.array([]), np.array([]), np.array([]), np.array([]),
            np.array([]), np.array([]), np.array([]), np.array([])
        ]
        for i in range(int(size/8)):
            for j in range(8):
                bit[j] = np.append(bit[j],array[i * 8 + j])
        for i in range(8):
            bit[i] = bit[i].reshape((int(np.sqrt(size / 8)), int(np.sqrt(size / 8))))
        self.flat = np.array(bit)
    def save(self,fname):
        img = Image.fromarray(self.array)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img.save(fname)
    def show(self):
        img = Image.fromarray(self.array)
        img.show()
    def change(self,data,num):
        self.flat[num] = data.array

class BitImg:
    def __init__(self,array):
        self.flat = array
        self.array = np.array([])
    def create_img(self,X,Y):
        (size_y,size_x) = self.flat.shape
        self.flat = self.flat.reshape((-1,))
        all_size = int(size_x*size_y/2)
        self.flat = self.flat[:all_size]
        array = []
        for i in range(int(all_size/8)):
            array.append(0)
            flag = 0b1
            for j in range(8):
                array[i] += self.flat[j+i*8]*flag
                flag = flag<<1
        self.array = np.array(array)
        self.array = self.array.reshape((Y,X))
        img = Image.fromarray(self.array).show()
        