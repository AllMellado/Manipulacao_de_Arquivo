import shutil
import re
import os

filepath = r"M:\Downloads\Stuff\test"


for folder in os.listdir(filepath):
    file = open(filepath + "\\" + folder + '\\info.txt', 'r', encoding="utf8")
    fileInfo = file.readlines()
    file.close()

    if len(fileInfo) < 7:
        continue

    title = fileInfo[1].split(':')[1][:-1]
    title = re.sub(r'[\\/\:*"<>\|\.%\$\^&£?]', '', title)
    artist = fileInfo[2].split(':')[1][:-1]
    # language = fileInfo[3].split(':')[1][:-1]
    magazine = fileInfo[4].split(':')[1][:-1]
    # publisher = fileInfo[5].split(':')[1][:-1]

    tags = ""
    for tag in fileInfo[7:]:
        if (tag != "tag:uncensored\n" and
                tag != "tag:unlimited\n" and
                tag != "tag:hentai\n" and
                tag != "tag:manga\n" and
                tag != "tag:condom\n" and
                tag != "tag:creampie\n" and
                tag != "tag:x-ray\n" and
                tag != "tag:fingering\n" and
                tag != "tag:doujin\n" and
                tag != "tag:pubic hair\n" and
                tag != "tag:bukkake\n" and
                tag != "tag:swimsuit\n" and
                tag != "tag:stockings\n" and
                tag != "tag:fangs\n" and
                tag != "tag:ponytail\n" and
                tag != "tag:hairy armpit\n" and
                tag != "tag:handjob\n" and
                tag != "tag:lingerie\n" and
                tag != "tag:sixty-nine\n" and
                tag != "tag:cunnilingus\n" and
                tag != "tag:paizuri\n" and
                tag != "tag:love hotel\n" and
                tag != "tag:twintails\n" and
                tag != "tag:eyebrows\n"):
            tags += tag.split(":")[1][:-1] + ","

    if os.path.exists(filepath + "\\" + folder + "\\cover.jpg"):
        os.remove(filepath + "\\" + folder + "\\cover.jpg")

    fileName = "[" + artist + "] " + title + " (" + magazine + ")" + tags

    src = filepath + "\\" + folder
    if os.path.exists(filepath + "\\" + fileName):
        dsc = filepath + "\\" + folder+"X"
    else:
        dsc = filepath + "\\" + fileName

    if len(dsc) > 255:
        dsc = filepath + "\\" + folder + "@"

    os.rename(src, dsc)
