import Utilities as ut

class TsQueryGenerator:

    def __init__(self,tbn='TableName'):
        
        uc_tbn = ut.uncapitalize(tbn)
        self.query = \
            'const '+uc_tbn+' = {\n' + \
            '  type: '+tbn+'Type,\n' + \
            '  args: {\n' + \
            '    id: { type: new GraphQLNonNull(GraphQLID) },\n' + \
            '  },\n' + \
            '  resolve: (\n' + \
            '    _: GraphQLSchema,\n' + \
            '    { id }: { id: string },\n' + \
            '    { viewer }: { viewer: Common.Viewer },\n' + \
            '  ) => {\n' + \
            '    return '+tbn+'.findById(viewer, id);\n' + \
            '  },\n' + \
            '};\n\n'

        self.wholeContent = \
            'import { GraphQLID, GraphQLNonNull, GraphQLSchema } from \'graphql\';\n' + \
            'import '+tbn+' from \'../'+tbn+'\';\n' + \
            'import '+tbn+'Type from \'../types/'+tbn+'Type\';\n\n' + \
            self.query + \
            'export default '+uc_tbn+';\n'

if __name__ == '__main__':
    tsq = TsQueryGenerator('MarketingActivity')
    f = open('MAQ.ts','w')
    f.write(tsq.wholeContent)
