import json

def createJSON(data, filename, subfolder):
    with open(subfolder + '\\' + filename, 'w', encoding="utf8") as outfile:
        json.dump(data, outfile, indent=4)

def openJSON(filename, subfolder):
    try:
        with open(subfolder + '\\' + filename, encoding="utf8") as json_file:
            openedFile = json.load(json_file)
        return openedFile
    except:
        return []

