import Utilities as ut

class TsCreateGenerator:

    def __init__(self,tbn='TableName'):
        
        self.query = \
            'const create'+tbn+' = {\n' + \
            '  type: '+tbn+'Type,\n' + \
            '  args: {\n' + \
            '    input: { type: new GraphQLNonNull('+tbn+'InputType) },\n' + \
            '  },\n' + \
            '  resolve: async (\n' + \
            '    _: GraphQLSchema,\n' + \
            '    { input }: { input: I'+tbn+'InputType },\n' + \
            '    { viewer }: { viewer: Common.Viewer },\n' + \
            '  ) => {\n' + \
            '    return '+tbn+'.createOne(viewer, input);\n' + \
            '  },\n' + \
            '};\n\n'

        self.wholeContent = \
            'import { GraphQLNonNull, GraphQLSchema } from \'graphql\';\n' + \
            'import '+tbn+' from \'../'+tbn+'\';\n' + \
            'import '+tbn+'InputType, {\n' + \
            '  I'+tbn+'InputType,\n' + \
            '} from \'../types/'+tbn+'InputType\';\n' + \
            'import '+tbn+'Type from \'../types/'+tbn+'Type\';\n\n' + \
            self.query + \
            'export default create'+tbn+';\n'

if __name__ == '__main__':
    tsc = TsCreateGenerator('MarketingActivity')
    f = open('MAC.ts','w')
    f.write(tsc.wholeContent)
