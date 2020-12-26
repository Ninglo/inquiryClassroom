import xlrd
import json


def main():
    roomUsage = {}
    """
        roomUsage = {
            date: classRoomName
        }
    """
    roomUsage = readFile('1.xls', roomUsage)
    roomUsage = readFile('2.xlsx', roomUsage)
    saveData(roomUsage)
    encodeFile('classroomData.json')


def readFile(filePath, roomUsage):
    """
        * filePath (str) 文件的相对 / 绝对路径
        * roomUsage (dict) 存储
    """
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
            roomUsage[scv(rowx=row, colx=0)].append(scv(rowx=row, colx=9))
        except KeyError:
            roomUsage[scv(rowx=row, colx=0)] = [scv(rowx=row, colx=9)]
    return roomUsage


def saveData(roomUsage):
    with open('classroomData.json', 'w+', encoding='utf-8') as f:
        formatUsageDic = {}
        indexList = []
        for key, value in roomUsage.items():
            indexList.append(key)
            formatUsageDic[key] = sorted(list(set(value)))
        # f.write(roomUsageJSON)
        formatUsageDic['name'] = 'classroomData'
        f.write(json.dumps(formatUsageDic))
        # print(indexList)

    timeMap = {}
    dateIndex = []

    for date in roomUsage.keys():
        try:
            dayEnd = date.find('日') + 1
            dateByMouthDay = date[:dayEnd]
            timeMap[dateByMouthDay].append(date)
        except KeyError:
            dateIndex.append(dateByMouthDay)
            timeMap[dateByMouthDay] = [date]
    dateDic = {
        'index': sorted(dateIndex),
        'name': 'dateIndex'
    }
    timeMap['name'] = 'timeIndex'

    with open('timeIndex.json', 'w+', encoding='utf-8') as f:
        f.write(str(timeMap).replace('\'', '\"'))

    with open('dateIndex.json', 'w+', encoding='utf-8') as f:
        f.write(str(dateDic).replace('\'', '\"'))


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
