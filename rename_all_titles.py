import os
import pathlib

filepath = r"C:\Downloads\Stuff"

for filename in os.listdir(filepath):
    if filename[-1] != "z":
        continue
    for c, char in enumerate(filename):
        if char == '[':
            start = c + 1
        if char == ']':
            end = c
            break

    src = filepath + "\\" + filename
    dsc = filepath + "\\" + filename[:-4] + " - " + filename[start:end] + ".cbz"
    os.rename(src, dsc)
