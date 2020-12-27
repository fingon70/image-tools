import sys
import os
from app import SimilarImages, SortImages


if __name__ == "__main__":
    if sys.argv[1] == "sort":
        if os.path.isdir(sys.argv[2]):
            sort_images = SortImages(sys.argv[2])
            sort_images.to_subfolder()
        else:
            print('Please pass directory name')

    elif sys.argv[1] == "similar":
        if os.path.isdir(sys.argv[2]):
            similar_images = SimilarImages(sys.argv[2])
            similar_images.find()
