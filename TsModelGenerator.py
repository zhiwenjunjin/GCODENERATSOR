class TsModelGenerator:

    def __init__(self,tbn='TableName',listOfParam=[],allString=True):

        self.importHeader = \
            'import * as mongoose from \'mongoose\';\n\n'

        self.essentialParam = \
            '  id: string;\n' + \
            '  created: Date;\n'

        self.addedParam = ''
        self.interfaceParam(listOfParam,allString)

        self.mainInterfaceString = \
            'interface I'+tbn+' {\n' + \
            self.essentialParam + \
            self.addedParam + \
            '}\n\n'

        self.mainInterfaceStringDocument = \
            'interface I'+tbn+'Document\n' + \
            '  extends mongoose.Document,\n' + \
            '    I'+tbn+' {\n' + \
            '  id: string;\n' + \
            '  toJSON(): I'+tbn+';\n' + \
            '}\n\n'

        uc_tbn = self.uncapitalize(tbn)
        self.schemaAddedParam = ''
        self.schemaParam(listOfParam,allString)
        self.mainSchema = \
            'const '+uc_tbn+'Schema = new mongoose.Schema(\n' + \
            '  {' + \
            '    created: { type: Date, default: Date.now },\n' + \
            self.schemaAddedParam + \
            '  },\n' + \
            '  {\n' + \
            '    collection: \''+uc_tbn+'s\',\n' + \
            '  },\n' + \
            ');\n\n'

        self.mainModel = \
            'const '+tbn+'Model = mongoose.model<I'+tbn+'Document>(\n' + \
            '  \''+tbn+'\',\n' + \
            '  '+uc_tbn+'Schema,\n' + \
            ');\n\n'

        self.footer = \
            'export default '+tbn+'Model;\n' + \
            'export { I'+tbn+' };\n'

        self.wholeContent = self.importHeader + \
            self.mainInterfaceString + \
            self.mainInterfaceStringDocument + \
            self.mainSchema + \
            self.mainModel + \
            self.footer


    def uncapitalize(self,tbn):
        return tbn[:1].lower() + tbn[1:] if tbn else ''
    
    def interfaceParam(self,listOfParam,allString):
        # default all parameters to string
        if allString:
            for item in listOfParam:
                self.addedParam += '  ' + str(item) + ': string;\n'

    def schemaParam(self,listOfParam,allString):
        # default all parameters to string
        if allString:
            for item in listOfParam:
                self.schemaAddedParam += '    ' + str(item) + \
                ': { type: String },\n'

if __name__ == '__main__':
    tsm = TsModelGenerator('MarketingActivity',['title','person'])
    # print(type(tsm.mainInterfaceString))
    f = open('MarketingAc.ts','w')
    f.write(tsm.wholeContent)