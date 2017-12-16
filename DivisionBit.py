import numpy as np
from PIL import Image

class DivisionBit:
    def __init__(self,array):
        self.array = array
        (self.y,self.x) = array.shape
        self.first = np.zeros((self.y,self.x))
        self.second = np.zeros((self.y,self.x))
        self.third = np.zeros((self.y,self.x))
        self.forth = np.zeros((self.y,self.x))
        self.fifth = np.zeros((self.y,self.x))
        self.sixth = np.zeros((self.y,self.x))
        self.seventh = np.zeros((self.y,self.x))
        self.eighth = np.zeros((self.y,self.x))
    def deivide(self):
        self.first = np.where(self.array & 0b1,1,0)
        self.second = np.where(self.array & 0b10,1,0)
        self.third = np.where(self.array & 0b100, 1, 0)
        self.forth = np.where(self.array & 0b1000, 1, 0)
        self.fifth = np.where(self.array & 0b10000,1,0)
        self.sixth = np.where(self.array & 0b100000,1,0)
        self.seventh = np.where(self.array & 0b1000000,1,0)
        self.eighth = np.where(self.array & 0b10000000,1,0)
    def show_all(self):
        Image.fromarray(self.first * 255).show()
        Image.fromarray(self.second * 255).show()
        Image.fromarray(self.third * 255).show()
        Image.fromarray(self.forth * 255).show()
        Image.fromarray(self.fifth * 255).show()
        Image.fromarray(self.sixth * 255).show()
        Image.fromarray(self.seventh * 255).show()
        Image.fromarray(self.eighth * 255).show()
    def match(self):
        self.array = np.zeros((self.y,self.x))
        self.array = self.array+self.first*0b1
        self.array = self.array+self.second*0b10
        self.array = self.array+self.third*0b100
        self.array = self.array+self.forth*0b1000
        self.array = self.array+self.fifth*0b10000
        self.array = self.array+self.sixth*0b100000
        self.array = self.array+self.seventh*0b1000000
        self.array = self.array+self.eighth*0b10000000
        Image.fromarray(self.array).show()
    def set_flat(self):
        flat_array = self.first.reshape(-1,)
        print("----------------------------")
        print(flat_array.shape)
        print(flat_array)
        print("----------------------------")
        flat_array = np.append(flat_array, self.second.reshape(-1,))
        flat_array = np.append(flat_array, self.third.reshape(-1,))
        flat_array = np.append(flat_array, self.forth.reshape(-1,))
        flat_array = np.append(flat_array, self.fifth.reshape(-1,))
        flat_array = np.append(flat_array, self.sixth.reshape(-1,))
        flat_array = np.append(flat_array, self.seventh.reshape(-1,))
        flat_array = np.append(flat_array, self.eighth.reshape(-1,))
        print(flat_array)
        flat_array = np.append(flat_array,flat_array)
        print("flat")
        print(flat_array.shape)
        print(self.y)
        print(self.y*self.x)
        print(self.array.shape)
        self.array = flat_array.reshape((self.y*4,self.x*4))
        Image.fromarray(self.array*255).show()
        
