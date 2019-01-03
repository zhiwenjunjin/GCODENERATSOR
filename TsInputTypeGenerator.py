class TsInputTypeGenerator:

    def __init__(self,tbn='TableName',listOfParam=[],allString=True):

        self.interParams = self.interfaceParam(listOfParam,allString)
        self.mainIInput = \
            'interface I'+tbn+'InputType {\n' + \
            self.interParams + \
            '}\n\n'

        self.inputParams = self.inputTypeParam(listOfParam,allString)
        self.mainInputType = \
            '/* add descriptions here */\n' + \
            'const '+tbn+'InputType = new GraphQLInputObjectType({\n' + \
            '  name: \''+tbn+'Input\',\n' + \
            '  fields: () => ({\n' + \
            self.inputParams + \
            '  }),\n' + \
            '});\n\n'

        self.wholeContent = \
            'import {\n' + \
            '  GraphQLInputObjectType,\n' + \
            '  GraphQLString,\n' + \
            '} from \'graphql\';\n' + \
            '/* add header here */\n\n' + \
            self.mainIInput + \
            self.mainInputType + \
            'export default '+tbn+'InputType;\n' + \
            'export { I'+tbn+'InputType };\n'
            
    def interfaceParam(self,listOfParam,allString):
        s = ''
        if allString:
            for item in listOfParam:
                s += '  '+str(item)+': string;\n'
        return s

    def inputTypeParam(self,listOfParam,allString):
        s = ''
        if allString:
            for item in listOfParam:
                s += '    '+str(item)+': {\n' + \
                    '      type: GraphQLString,\n' + \
                    '      description: \'\',\n' + \
                    '    },\n'
        return s

if __name__ == '__main__':
    tsi = TsInputTypeGenerator('MarketingActivity',['title','person'])
    f = open('MAIT.ts','w')
    f.write(tsi.wholeContent)