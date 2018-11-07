class TsModelGenerator:

    def __init__(self,tbn='TableName',listOfParam=[],allString=True):

        self.essentialParam = \
            '  id: string;\n' + \
            '  created: Date;\n'

        self.addedParam = ''
        self.interfaceParam(listOfParam,allString)

        self.mainInterfaceString = \
            'interface I'+tbn+' {\n' + \
            self.essentialParam + \
            self.addedParam + \
            '}\n'
    
    def interfaceParam(self,listOfParam,allString):
        if allString:
            for item in listOfParam:
                self.addedParam += '  ' + str(item) + ': string;\n'


if __name__ == '__main__':
    tsm = TsModelGenerator('MarketingActivity',['title','person'])
    # print(type(tsm.mainInterfaceString))
    f = open('MarketingAc.ts','w')
    f.write(tsm.mainInterfaceString)