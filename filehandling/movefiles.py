import os
import shutil

folders = {0: "first", 1: "second", 2: "third", 3: "fourth"}

if __name__ == '__main__':

    for item in folders:
        print(item)
        print(folders.get(item))

    _root = "c:\\fuji"
    if os.path.isdir(_root):
        print("listdir: %s" % os.listdir(path=_root))

    for folder in folders:
        _path = os.path.join(_root, folders.get(folder))
        print("path: %s" % _path)
        for _file in os.listdir(path=_path):
            if not os.path.isdir(_file):
                print("Original file: %s" % _file)
                _file_dest = _file.split('.')[0] + '_' + str(folder) + '.bmp'
                print("Destination file: %s" % _file_dest)
                shutil.move(os.path.join(_path, _file), os.path.join(_root, _file_dest))
