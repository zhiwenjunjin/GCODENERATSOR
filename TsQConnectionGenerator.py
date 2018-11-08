import Utilities as ut

class TsQConnectionGenerator:

    def __init__(self,tbn='TableName'):
        
        uc_tbn = ut.uncapitalize(tbn)
        self.query = \
            'const '+uc_tbn+'Connection = {\n' + \
            '  type: connectionDefault('+tbn+'ConnectionType),\n' + \
            '  args: connectionCustomArgs,\n' + \
            '  resolve: (\n' + \
            '    _: GraphQLSchema,\n' + \
            '    args: IPageArgs,\n' + \
            '    { viewer }: { viewer: Common.Viewer },\n' + \
            '  ) {\n' + \
            '    return '+tbn+'.connectionSearch(viewer, args);\n' + \
            '  },\n' + \
            '};\n\n'

        self.wholeContent = \
            'import { GraphQLSchema } from \'graphql\';\n' + \
            'import connectionDefault, {\n' + \
            '  connectionCustomArgs,\n' + \
            '  IPageArgs,\n' + \
            '} from \'../../Pagniation/types/PaginationType\';\n' + \
            'import '+tbn+' from \'../'+tbn+'\';\n' + \
            'import '+tbn+'sConnectionType from \'../types/'+tbn+'Type\';\n\n' + \
            self.query + \
            'export default '+uc_tbn+'sConnection;\n'

if __name__ == '__main__':
    tsqc = TsQConnectionGenerator('MarketingActivity')
    f = open('folder/MAQC.ts','w')
    f.write(tsqc.wholeContent)
