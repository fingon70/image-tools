from exif import Image
import os


def __get_date(file):
    with open(file, 'rb') as image_file:
        image = Image(image_file)
        if image.has_exif:
            date_time = image.datetime.split(' ')
            return date_time[0].replace(':', '-')


def __img_to_date_subdir(subdir, file_path, file):
    file_dest_path = os.path.join(subdir, file)

    if not os.path.isdir(subdir):
        os.mkdir(subdir)
    
    if not os.path.isdir(file_dest_path):
        os.rename(file_path, file_dest_path)
        return True
    
    return False


def __sort_to_subdir(dir_name):
    file_list = os.listdir(dir_name)

    for file in file_list:
        if file.lower().endswith('.jpg'):
            complete_path = os.path.join(dir_name, file)
            date = __get_date(complete_path)
            try:
                subdir = os.path.join(dir_name, date)

                if __img_to_date_subdir(subdir, complete_path, file):
                    print(f'File {file} moved to {subdir}')
                else:
                    print(f'Sorting for {file} failed')
            except:
                print(f'Skip: Wrong date {file} in {dir_name}')


def sort_images(dir):
    if os.path.isdir(dir):
        __sort_to_subdir(dir)
    else:
        print('Please pass directory name')