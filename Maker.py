import Data as data
def makeRqTable(rqTable): #rqTable 입력하면 csv 파일 형태로 생성
    f = open("result/rqTable.csv", "w")
    for str in rqTable.type:
        if str.__eq__("filePath"):
            f.write(str + "\n")
        else:
            f.write(str + ",")

    for rq in rqTable.rqList:
        f.write(rq.toString() + "\n")
    f.close()


def makeUseCaseSpec(uc):
    # y : 6, N
    table = []
    sys = uc.system
    table.append(Line.makeArray(["Usecase Specific"]))
    table.append(Line.makeArray(["Usecase Name", uc.id+"_name"]))
    table.append(Line.makeArray(["System Id", sys.id]))
    table.append(Line.makeArray(["UC Id", uc.id]))
    table.append(Line.makeArray(["desc", uc.desc]))
    table.append(Line.makeArray(["Use Actor", uc.useActor]))
    table.append(Line.makeArray(["Related Rq", '"' + ", ".join(uc.rqList) + '"']))
    table.append(Line.makeArray(["Pre-Condition", uc.preCond]))
    table.append(Line.makeArray(["Post-Condition", uc.postCond]))
    table.append(Line.makeArray([]))
    table.append(Line.makeArray(["Scenario"]))
    table.append(Line.makeArray(["Sequence Name", "context", "Pre-Condition", "Post-Condition", "Host", "Client"]))
    for fl in uc.flowList:
        table.append(Line.makeArray([fl.sequenceName, fl.desc, fl.preCond, fl.postCond, fl.host, fl.client]))

    f = open("result/"+sys.id + "-" + uc.id + ".csv", "w")
    for line in table:
        for data in line:
            f.write(data + ",")
        f.write("\n")
    f.close()

class Line:
    size = 6

    @staticmethod
    def makeArray(strList):
        dataNum = len(strList)
        csvLine = strList[:]

        while dataNum < Line.size:
            csvLine.append("")
            dataNum += 1
        return csvLine

rqTable = data.RqTable()
makeRqTable(rqTable)
sysList = []
for i in range(5):
    sysList.append(data.System())
for sys in sysList:
    for uc in sys.useCaseList:
        makeUseCaseSpec(uc)


"Usecase Spec,,,,"

