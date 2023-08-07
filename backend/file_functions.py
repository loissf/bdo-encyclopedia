import json
import csv

def createJSON(data, filename, subfolder):
    with open(subfolder + '\\' + filename, 'w', encoding="utf8") as outfile:
        json.dump(data, outfile, indent=4)

def openJSON(filename, subfolder):
    try:
        with open(subfolder + '\\' + filename, encoding="utf8") as json_file:
            openedFile = json.load(json_file)
        return openedFile
    except:
        return {}

def readCsv(filename, subfolder, newline='', delimiter=',', quotechar='"', hasHeader=True):
    try:
        with open(subfolder + '\\' + filename, mode="r", encoding="utf8", newline=newline) as csvfile:
            spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)

            header: list[str] = []
            rows: list[list[str]] = []
            
            if(hasHeader):
                header = spamreader.__next__()

            for row in spamreader:
                rows.append(row)

            return ( header, rows )
    except:
        return None