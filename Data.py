import random
import numpy as np


class Requirement:
    def __init__(self, id):
        self.id = id  # RQ-num
        self.desc = id + "'s desc."
        self.name = id + "'s Name"
        if random.randrange(0, 101) < 70:
            self.type = "Functional"
        else:
            self.type = "Non-Functional"

        self.department = random.choice(['Team A', 'Team B', 'Team C', 'Team D', 'Team E', 'Team F'])
        self.filePath = "201.248.87.55/requirement/" + id;

    def toString(self):
        return self.id + "," + self.desc + "," + self.name + "," + self.type + "," + self.department + "," + self.filePath


class RqTable:
    """
    기본 생성자로 50~100 사이즈의 테이블 생성
    """
    def rqTableMake(self):
        self.id = "";
        self.desc = "desc"
        self.dep = "dep"

    def __init__(self):
        self.rqList = []
        self.size = random.randrange(50, 100)
        self.type = ["ID", "desc", "name", "type", "depertment", "filePath"]
        self.datas = []
        num = 1
        while num <= self.size:
            self.datas.append(self.rqDataMake(num))
            num += 1

    def rqDataMake(self, num):
        id = "RQ-" + str(num)
        req = Requirement(id)
        self.rqList.append(req)
        return [req.id, req.desc, req.name, req.type, req.department, req.filePath]

class Usecase:
    ucNum = 1
    flowNum = 8
    relatedRqNum = 4

    @staticmethod
    def makeRqList(rqSource, choiceNum):
        rqList = []
        source = np.arange(0, System.relatedRqNum)
        random.shuffle(source)

        select = sorted(source[0:choiceNum])
        for i in select:
            rqList.append(rqSource[i])
        return rqList

    def __init__(self, id, relatedRq, useActor, system):
        self.system = system
        self.id = id
        self.name = id
        self.rqList = relatedRq
        self.desc = self.id + "'s desc"
        self.preCond = self.id + "'s pre condition."
        self.postCond = self.id + "'s post Condition"
        self.useActor = useActor
        self.createFlowList()

    def createFlowList(self):
        self.flowList = []
        seqName = "flow1()"
        num = 2
        desc = "1. " + self.useActor + " use " + seqName + " on " + self.system.id

        flow = Flow(seqName, desc)
        flow.setActor(self.useActor)

        #self.getNextType()
        self.flowList.append(flow)

        while num < Usecase.flowNum:
            desc = str(num) + ". " + self.system.id + " do Flow" + str(num) + "."
            seqName = "flow" + str(num) + "()"
            flow = Flow(seqName, desc)
            self.flowList.append(flow)
            num += 1

class System:
    systemNum = 1
    relatedRqNum = 15
    usecaseNum = 10

    def __init__(self, rqSize):
        self.id = "Sys" + str(System.systemNum)
        self.name = self.id
        self.setRq(rqSize)
        self.setUsecase(System.usecaseNum)
        System.systemNum += 1

    def setRq(self, rqSize):
        self.rqList = []
        source = np.arange(1, rqSize + 1)
        random.shuffle(source)

        select = sorted(source[0:System.relatedRqNum])

        for i in range(System.relatedRqNum):
            rqId = "RQ-" + str(select[i])
            self.rqList.append(rqId)
        print(self.rqList)
        # print("set Rq", rqSize)

    def setUsecase(self, ucNum):
        self.useCaseList = []
        i = 0
        while i < ucNum:
            i += 1
            id = "UC-" + str(i)
            rqList = Usecase.makeRqList(self.rqList, Usecase.relatedRqNum)
            actor = "Actor-1"
            self.useCaseList.append(Usecase(id, rqList, actor, self))


class Flow:
    def __init__(self, seqName, desc):
        self.desc = desc
        self.sequenceName = seqName
        self.postCond = ""
        self.preCond = ""
        self.host = ""
        self.client = ""

    def setActor(self, useActor):
        self.client = useActor

"""
index = 0
slist = []
while index < 10:
    slist.append(System(50))
    index += 1

for data in slist:
    print(data.id)
"""

# class Scnarios:




# uc = Usecase("UC1", ["RQ-1", "RQ-3"], "Actor1", System(50))


"""
    def getNextType(self):
        r = random.
"""


# var = RqTable()