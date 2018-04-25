<<<<<<< HEAD
import os

date = []
openData = []
highData = []
lowData = []
closeData = []
adjCloseData = []
volumeData = []
percent_openData = []
percent_highData = []
percent_lowData = []
percent_closeData = []
percent_adjCloseData = []
percent_volumeData = []

def fill(tix):
    file = open(tix + ".csv", "r")

    for line in file:
        seperatedData = line.split(",")
        date.append(seperatedData[0])
        openData.append(float(seperatedData[1]))
        highData.append(float(seperatedData[2]))
        lowData.append(float(seperatedData[3]))
        closeData.append(float(seperatedData[4]))
        adjCloseData.append(float(seperatedData[5]))
        volumeData.append(int(seperatedData[6]))

    adjust()

def adjust():
    for x in range(1,len(closeData)):
        percent_openData.append((openData[x]/openData[x-1]) - 1)
        percent_highData.append((highData[x]/highData[x-1]) - 1)
        percent_lowData.append((lowData[x]/lowData[x-1]) - 1)
        percent_closeData.append((closeData[x]/closeData[x-1]) - 1)
        percent_adjCloseData.append((adjCloseData[x]/closeData[x-1]) - 1)
        percent_volumeData.append((volumeData[x]/volumeData[x-1]) - 1)

def trainingInputData():
    fullSet = []
    for x in range(0, len(percent_closeData)-1):
        fullSet.append([percent_openData[x], percent_highData[x], percent_lowData[x],
                        percent_closeData[x], percent_adjCloseData[x], percent_volumeData[x]])
    return fullSet

def trainingOutputData():
    fullSet = []

    for i in range(1,len(percent_closeData)):
        fullSet.append(percent_closeData[i])

    return fullSet

def get_current(config, trait):
    with open(config, 'r') as f:
        for ln in f:
            if ln.startswith(trait):
                return ln

def changeConfig(config, old, new, ID):
    text = ""
    with open(config, 'r') as base_file:
        text = base_file.readlines()
        base_file.close()

    write_path = 'config_{!r}'.format(ID)

    new_config = open(write_path, 'w')

    for line in text:
        if old in line:
            line = line.replace(old, new)
        new_config.write(line)
=======
import os

date = []
openData = []
highData = []
lowData = []
closeData = []
adjCloseData = []
volumeData = []
percent_openData = []
percent_highData = []
percent_lowData = []
percent_closeData = []
percent_adjCloseData = []
percent_volumeData = []

def fill(tix):
    file = open(tix + ".csv", "r")

    for line in file:
        seperatedData = line.split(",")
        date.append(seperatedData[0])
        openData.append(float(seperatedData[1]))
        highData.append(float(seperatedData[2]))
        lowData.append(float(seperatedData[3]))
        closeData.append(float(seperatedData[4]))
        adjCloseData.append(float(seperatedData[5]))
        volumeData.append(int(seperatedData[6]))

    adjust()

def adjust():
    for x in range(1,len(closeData)):
        percent_openData.append((openData[x]/openData[x-1]) - 1)
        percent_highData.append((highData[x]/highData[x-1]) - 1)
        percent_lowData.append((lowData[x]/lowData[x-1]) - 1)
        percent_closeData.append((closeData[x]/closeData[x-1]) - 1)
        percent_adjCloseData.append((adjCloseData[x]/closeData[x-1]) - 1)
        percent_volumeData.append((volumeData[x]/volumeData[x-1]) - 1)

def trainingInputData():
    fullSet = []
    for x in range(0, len(percent_closeData)-1):
        fullSet.append([percent_openData[x], percent_highData[x], percent_lowData[x],
                        percent_closeData[x], percent_adjCloseData[x], percent_volumeData[x]])
    return fullSet

def trainingOutputData():
    fullSet = []

    for i in range(1,len(percent_closeData)):
        fullSet.append(percent_closeData[i])

    return fullSet

def get_current(config, trait):
    with open(config, 'r') as f:
        for ln in f:
            if ln.startswith(trait):
                return ln

def changeConfig(config, old, new, ID):
    text = ""
    with open(config, 'r') as base_file:
        text = base_file.readlines()
        base_file.close()

    write_path = 'config_{!r}'.format(ID)

    new_config = open(write_path, 'w')

    for line in text:
        if old in line:
            line = line.replace(old, new)
        new_config.write(line)
>>>>>>> 00b35791e129996c8b4cb60ebab20409eab81683
    new_config.close()