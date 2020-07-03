import xlrd
import json


def main():
    roomUsage = {}
    roomUsage = readFile('ci.xls', roomUsage)
    roomUsage = readFile('gz.xlsx', roomUsage)
    saveData(roomUsage, 'data')
    encodeFile('data')


def readFile(filePath, roomUsage):
    book = xlrd.open_workbook(filePath)
    sheetNum = book.nsheets

    for i in range(sheetNum):
        sheet = book.sheet_by_index(i)
        roomUsage = readUsageBySheet(sheet, roomUsage)

    return roomUsage


def readUsageBySheet(sheet, roomUsage):
    scv = sheet.cell_value
    for row in range(1, sheet.nrows):
        try:
            roomUsage[scv(rowx=row, colx=0)].append(scv(rowx=row, colx=10))
        except KeyError:
            roomUsage[scv(rowx=row, colx=0)] = [scv(rowx=row, colx=10)]
    return roomUsage


def saveData(roomUsage, name):
    with open('{name}'.format(name=name), 'w+', encoding='utf-8') as f:
        #roomUsageList = []
        formatUsageDic = {}
        indexList = []
        for key, value in roomUsage.items():
            indexList.append(key)
            formatUsageDic[key] = sorted(list(set(value)))
        """
            dic = {
                "time": key,
                "room": sorted(list(set(value)))
            }
            roomUsageList.append(dic)
        roomUsageJSON = json.dumps(roomUsageList)
        """
        # f.write(roomUsageJSON)
        f.write(json.dumps(formatUsageDic))
        print(indexList)


def encodeFile(filePath):
    file_data = ""
    with open(filePath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.encode('utf-8').decode('unicode_escape')
            file_data += line
    with open(filePath, "w", encoding="utf-8") as f:
        f.write(file_data)


if __name__ == "__main__":
    main()
