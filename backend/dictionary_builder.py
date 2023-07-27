import csv
import os
from file_functions import createJSON

def importItems(path):
    dictionary = {}

    files = os.listdir(path)
    for file in files:
        rows = readCsv(file, path)
        header = rows.__next__()

        columns = {}

        for i in range(header.__len__()):
            columns[header[i]] = i

        for row in rows:
            try:
                dictionary[row[0]] = {
                    "id": row[columns["mainKey"]],
                    "name": row[columns["name"]],
                    "grade": row[columns["grade"]],
                    "main_category": row[columns["main_category_id"]],
                    "sub_category": row[columns["sub_category_id"]],
                }
            except Exception as e:
                print(header)
                print(row)
                print(e, "in", file)
                print("---------------------------")
    
    createJSON(dictionary, "items.json", "backend/import-result")
    

def readCsv(filename, subfolder, newline='', delimiter=',', quotechar='|'):
    with open(subfolder + '\\' + filename, mode="r", encoding="utf8", newline=newline) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        for row in spamreader:
            yield row


importItems("src/resources/item-data")