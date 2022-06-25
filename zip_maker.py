import shutil
import os
import re

filepath = r"M:\Downloads\Stuff"

for filename in os.listdir(filepath):
    if os.path.exists(filepath + "\\" + filename + ".cbz"):
        continue
    if "p" == filename[-1]:
        path = filepath + "\\" + filename
        src = path
        dst = path[:-4] + '.cbz'
        os.rename(src, dst)

    if "]" == filename[-1]:
        newZip = filepath + "\\" + filename
        shutil.make_archive(newZip, 'zip', newZip)

        src = newZip + ".zip"
        dst = newZip + ".cbz"
        os.rename(src, dst)
''



