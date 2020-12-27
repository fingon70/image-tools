from exif import Image
import os


class SortImages:
    def __init__(self, dirname):
        self.dirname = dirname

    def to_subfolder(self):
        """
        Move image files in given dir into subfolders by exif date
        """

        file_list = os.listdir(self.dirname)

        for file in file_list:
            if file.lower().endswith('.jpg'):
                filename = os.path.join(self.dirname, file)

                with open(filename, 'rb') as image_file:
                    image = Image(image_file)
                    if image.has_exif:
                        date_time = image.datetime.split(' ')
                        filedate = date_time[0].replace(':', '-')

                try:
                    subdir = os.path.join(self.dirname, filedate)

                    if self.__img_to_date_subdir(subdir, filename, file):
                        print(f'File {file} moved to {subdir}')
                    else:
                        print(f'Sorting for {file} failed')

                except:
                    print(f'Skip: Wrong date {file} in {self.dirname}')
            
            else:
                print(f'File {file} is not a JPEG image')

    def __img_to_date_subdir(self, subdir, filename, file):
        dest_filename = os.path.join(subdir, file)

        if not os.path.isdir(subdir):
            os.mkdir(subdir)

        if not os.path.isdir(dest_filename):
            os.rename(filename, dest_filename)
            return True

        return False
