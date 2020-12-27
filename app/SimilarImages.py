from PIL import Image
import os
import imagehash
import numpy as np


class SimilarImages:
    def __init__(self, dirname, similarity=80, hash_size = 8):
        self.dirname = dirname
        self.similarity = similarity
        self.hash_size = hash_size

    def find(self):
        for root, dirs, files in os.walk(self.dirname, topdown=False):
            for file in files:
                if file.lower().endswith('.jpg'):
                    filename = os.path.join(root, file)
                    filehash = self.__get_hash(filename)
                    nz = np.count_nonzero(filehash)
                    print(f'FILE: {filename}, NZ: {nz}')
            #for name in dirs:
                #print('DIR: ' + os.path.join(root, name))
    
    def __get_hash(self, filename):
        #threshold = 1 - self.similarity/100
        #diff_limit = int(threshold*(self.hash_size**2))

        with Image.open(filename) as img:
            #print(img)
            hash = imagehash.average_hash(img, self.hash_size).hash
            return hash
