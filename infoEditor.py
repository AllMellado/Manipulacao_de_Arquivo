import shutil
import re
import os
import json
from types import SimpleNamespace

filepath = r"M:\Downloads\nhentaiScrap\Scanned"

for fileName in os.listdir(filepath):
    print(fileName)
    file = open(filepath + "\\" + fileName, 'r+', encoding="utf8")
    fileInfo = file.readlines()

    if fileInfo[0][0] != "{":
        file.close()
        continue

    jsonData = json.loads(fileInfo[0])

    if 'error' in jsonData:
        continue

    title = jsonData["title"]
    engTitle = title["english"]
    engTitle = re.sub(r'[\/\t\\:\*\"\<\>\|\.\%\$\^\&\£\?]', '', engTitle)

    tagString = ""
    for tag in jsonData["tags"]:
        if tag["type"] == "tag":
            tagString += tag["name"] + ","
        else:
            tagString += tag["type"] + ":" + tag["name"] + ","

    file.seek(0)
    file.write(tagString)
    file.truncate()
    file.close()

    src = filepath + "\\" + fileName
    if os.path.exists(filepath + "\\" + engTitle+".json"):
        dsc = filepath + "\\" + "X" + fileName
    else:
        dsc = filepath + "\\" + engTitle+".json"

    if len(dsc) > 255:
        dsc = filepath + "\\" + "@" + fileName

    os.rename(src, dsc)

