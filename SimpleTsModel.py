import os
import TsModelGenerator
import TsClassGenerator
import TsInputTypeGenerator
import TsTypeGenerator
import Utilities as ut
import TsQueryGenerator
import TsQConnectionGenerator
import TsCreateGenerator
import TsIndexGenerator
import TsUpdateGenerator

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

        self.uc_tbn = ut.uncapitalize(self.tbn)
        queryFile = open(queriesDir+'/'+self.uc_tbn+'.ts','w')
        tsq = TsQueryGenerator.TsQueryGenerator(self.tbn)
        queryFile.write(tsq.wholeContent)

        qConnectionFile = open(queriesDir+'/'+self.uc_tbn+'sConnection.ts','w')
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

        self.gUpdate()

        indexFile = open(mainDir+'/index.ts','w')
        tsid = TsIndexGenerator.TsIndexGenerator(self.tbn)
        indexFile.write(tsid.wholeContent)

    def register(self):
        outterIndexFile = open(self.path+'index.ts','r')
        outterIndexString = outterIndexFile.read()
        newString = outterIndexString.replace( \
            '// INSERT IMPORT HERE', \
            'import {\n' + \
            '  create'+self.tbn+',\n' + \
            '  '+self.uc_tbn+',\n' + \
            '  '+self.uc_tbn+'sConnection,\n' + \
            '  update'+self.tbn+',\n' + \
            '} from \'./'+self.tbn+'\';\n\n' + \
            '// INSERT IMPORT HERE', \
            1 \
            )
        newString = newString.replace( \
            '// INSERT QUERY HERE', \
            self.uc_tbn+',\n' + \
            '        '+self.uc_tbn+'sConnection,\n' + \
            '        // INSERT QUERY HERE', \
            1 \
            )
        newString = newString.replace( \
            '// INSERT MUTATION HERE', \
            'create'+self.tbn+',\n' + \
            'update'+self.tbn+',\n' + \
            '        // INSERT MUTATION HERE', \
            1 \
            )
        outterIndexFile = open(self.path+'index.ts','w')
        outterIndexFile.write(newString)

        elasticSearchIndexFile = open(self.path+'ElasticSearch/index.ts','r')
        esIString = elasticSearchIndexFile.read()
        newString = esIString.replace( \
            '// INSERT CREATE CROSS HERE', \
            'case \''+self.tbn.lower()+'\':\n' + \
            '        data = await '+self.tbn+'.findCrossById(id);\n' + \
            '        await elasticCreate(index, data);\n' + \
            '        break;\n' + \
            '      // INSERT CREATE CROSS HERE', \
            1 \
            )
        newString = newString.replace(\
            '// INSERT UPDATE CROSS HERE', \
            'case \''+self.tbn.lower()+'\':\n' + \
            '        data = await '+self.tbn+'.findCrossById(id);\n' + \
            '        await elasticUpdate(index, data);\n' + \
            '        break;\n' + \
            '      // INSERT UPDATE CROSS HERE', \
            1 \
            )
        newString = newString.replace( \
            '// IMPORT MODULE HERE', \
            'import '+self.tbn+' from \'../'+self.tbn+'\';\n' + \
            '// IMPORT MODULE HERE', \
            1 \
            )
        elasticSearchIndexFile = open(self.path+'ElasticSearch/index.ts','w')
        elasticSearchIndexFile.write(newString)

    def gUpdate(self):
        tsu = TsUpdateGenerator.TsUpdateGenerator(self.tbn)
        updateFile = open(self.path+self.tbn+'/mutations/update'+self.tbn+'.ts','w')
        updateFile.write(tsu.wholeContent)

if __name__ == '__main__':
    stm = SimpleTsModel(
        path='/Users/junjinchen/Documents/GitHub/zhiwen-api/src/schema/',
        tbn='MarketingActivityWechatGroup',
        listOfParam=['marketingActivityId','groupName','peopleLimit','groupLeader','QRCode','QRCodeExpiredBy','Note']
        )
    stm.gUpdate()
    # stm.generate()
    # stm.register()