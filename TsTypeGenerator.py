class TsTypeGenerator:

    def __init__(self,tbn='TableName',listOfParam=[],allString=True):

        self.tp = self.typeParam(listOfParam,allString)
        self.mainType = \
            '/* add description here */\n' + \
            'const '+tbn+'Type = new GraphQLObjectType({\n' + \
            '  name: \''+tbn+'\',\n' + \
            '  fields: () => ({\n' + \
            '    id: { type: new GraphQLNonNull(GraphQLID) },\n' + \
            '    created: {\n' + \
            '      type: new GraphQLNonNull(GraphQLString),\n' + \
            '      resolve: ({ created }) =>\n' + \
            '        created && typeof created !== \'string\'\n' + \
            '          ? created.toISOString()\n' + \
            '          : created,\n' + \
            '    },\n' + \
            self.tp + \
            '  }),\n' + \
            '});\n\n'
        self.connectionType = self.mainType.replace(tbn,tbn+'Connection')

        self.wholeContent = \
            '/* add header here */\n' + \
            self.mainType + \
            self.connectionType + \
            'export { '+tbn+'ConnectionType };\n' + \
            'export default '+tbn+'Type;\n'

    def typeParam(self,listOfParam,allString):
        s = ''
        if allString:
            for item in listOfParam:
                s += '    '+str(item)+': {\n' + \
                    '      type: GraphQLString,\n' + \
                    '      description: \'\',\n' + \
                    '    },\n'
        return s

if __name__ == '__main__':
    tst = TsTypeGenerator('MarketingActivity',['title','person'])
    f = open('MAT.ts','w')
    f.write(tst.wholeContent)