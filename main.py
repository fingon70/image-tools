import sys
import app

if __name__ == "__main__":
    if sys.argv[1] == "sort":
        app.sort_images(sys.argv[2])