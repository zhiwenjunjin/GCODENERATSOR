import os
import TsModelGenerator
import TsClassGenerator
import TsInputTypeGenerator
import TsTypeGenerator
import Utilities as ut
import TsQueryGenerator
import TsQConnectionGenerator
import TsCreateGenerator

class SimpleTsModel:

    def __init__(self,path,tbn='TableName',listOfParam=[],allString=True):

        self.path = path
        self.tbn = tbn
        self.listOfParam = listOfParam
        self.allString = allString

    def generate(self):

        mainDir = self.path + self.tbn
        try:
            os.mkdir(mainDir)
            print('main dir successful')
        except FileExistsError:
            print('fk this path')

        modelFile = open(mainDir+'/'+self.tbn+'Model.ts','w')
        tsm = TsModelGenerator.TsModelGenerator(self.tbn,self.listOfParam,self.allString)
        modelFile.write(tsm.wholeContent)

        classFile = open(mainDir+'/'+self.tbn+'.ts','w')
        tsc = TsClassGenerator.TsClassGenerator(self.tbn)
        classFile.write(tsc.wholeContent)

        typesDir = mainDir + '/types'
        try:
            os.mkdir(typesDir)
            print('types dir successful')
        except FileExistsError:
            print('fk this types path')

        inputTypeFile = open(typesDir+'/'+self.tbn+'InputType.ts','w')
        tsi = TsInputTypeGenerator.TsInputTypeGenerator(self.tbn,self.listOfParam,self.allString)
        inputTypeFile.write(tsi.wholeContent)

        typeFile = open(typesDir+'/'+self.tbn+'Type.ts','w')
        tst = TsTypeGenerator.TsTypeGenerator(self.tbn,self.listOfParam,self.allString)
        typeFile.write(tst.wholeContent)

        queriesDir = mainDir + '/queries'
        try:
            os.mkdir(queriesDir)
            print('queries dir successful')
        except FileExistsError:
            print('fk this queries path')

        uc_tbn = ut.uncapitalize(self.tbn)
        queryFile = open(queriesDir+'/'+uc_tbn+'.ts','w')
        tsq = TsQueryGenerator.TsQueryGenerator(self.tbn)
        queryFile.write(tsq.wholeContent)

        qConnectionFile = open(queriesDir+'/'+uc_tbn+'sConnection.ts','w')
        tsqc = TsQConnectionGenerator.TsQConnectionGenerator(self.tbn)
        qConnectionFile.write(tsqc.wholeContent)

        mutationsDir = mainDir + '/mutations'
        try:
            os.mkdir(mutationsDir)
            print('mutations dir successful')
        except FileExistsError:
            print('fk this mutations path')

        createFile = open(mutationsDir+'/create'+self.tbn+'.ts','w')
        tscr = TsCreateGenerator.TsCreateGenerator(self.tbn)
        createFile.write(tscr.wholeContent)

        # print(os.path.exists(''))
        # try:
        #     os.mkdir('')
        #     print('successful')
        # except FileExistsError:
        #     print('fk this dir')

if __name__ == '__main__':
    stm = SimpleTsModel(
        path='/Users/junjinchen/Documents/GitHub/zhiwen-api/src/schema/',
        tbn='SimpleModel',
        listOfParam=['OK','NoProb']
        )
    stm.generate()