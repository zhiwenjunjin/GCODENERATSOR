import Utilities as ut

class TsClassGenerator:

    def __init__(self,tbn='TableName'):
        
        self.findFunction = \
            '  public static async find(_: Common.Viewer, args: object) {\n' + \
            '    return '+tbn+'Model.find(args);\n' + \
            '  }\n'
        self.findOneFunction = \
            '  public statci async findOne(_: Common.Viewer, args: object) {\n' + \
            '    return '+tbn+'Model.findOne(args);\n' + \
            '  }\n'
        self.findByIdFunction = \
            '  public static async findById(\n' + \
            '    _: Common.Viewer,\n' + \
            '    id: string | mongoose.Types.ObjectId,\n' + \
            '  ) {\n' + \
            '    return '+tbn+'Model.findById(id);\n' + \
            '  }\n'
        uc_tbn = ut.uncapitalize(tbn)
        self.findRawByIdFunction = \
            '  public static async findRawById(id: string | mongoose.Types.ObjectId) {\n' + \
            '    const '+uc_tbn+' = await '+tbn+'Model.findById(id, \'-__v\');\n' + \
            '    if (!'+uc_tbn+') {\n' + \
            '      throw new Error(/*add error message here*/);\n' + \
            '    }\n' + \
            '    const '+uc_tbn+'Json = {\n' + \
            '      ...omit('+tbn+'.toJSON(), \'_id\'),\n' + \
            '      id: '+uc_tbn+'.id,\n' + \
            '    };\n' + \
            '    return '+uc_tbn+'Json;\n' + \
            '  }\n'
        self.findCrossByIdFunction = \
            '  public static async findCrossById(id: string | mongoose.Types.ObjectId) {\n' + \
            '    const '+uc_tbn+'Json = await this.findRawById(id);\n' + \
            '    return {\n' + \
            '      ...'+uc_tbn+'Json,\n' + \
            '    };\n' + \
            '  }\n\n'

        lrc_tbn = ut.lower_case(tbn)
        self.createOneFunction = \
            '  public static async createOne(\n' + \
            '    viewer: Common.Viewer,\n' + \
            '    input: I'+tbn+'InputType,\n' + \
            '  ) {\n' + \
            '    if (!viewer) {\n' + \
            '      throw new Error(\'Unauthorized\');\n' + \
            '    }\n' + \
            '    try {\n' + \
            '      /* add restriction here */\n' + \
            '      const '+uc_tbn+'Doc = new '+tbn+'Model({\n' + \
            '        ...input,\n' + \
            '      });\n' + \
            '      try { \n' + \
            '        const '+uc_tbn+' = await '+uc_tbn+'Doc.save();\n' + \
            '        await elasticCreateCross(\''+lrc_tbn+'\', '+uc_tbn+'Doc.id);\n' + \
            '        return '+uc_tbn+';\n' + \
            '      } catch (e) {\n' + \
            '         throw e;\n' + \
            '      }\n' + \
            '    } catch(e) {\n' + \
            '       throw e;\n' + \
            '    }\n' + \
            '  }\n\n'

        self.connectionSearchFunction = \
            '  public static async connectionSearch(\n' + \
            '    viewer: Common.Viewer,\n' + \
            '    args: Common.PageArgs,\n' + \
            '  ) {\n' + \
            '    const newArgs = formatArgs(args);\n' + \
            '    const data = await connectionSearch(newArgs, {\n' + \
            '      index: \''+lrc_tbn+'\',\n' + \
            '      type: \''+lrc_tbn+'\',\n' + \
            '    });\n' + \
            '    return data;\n' + \
            '  }\n'


        self.wholeContent = \
            '/* add headers here */\n' + \
            'class '+tbn+' {\n' + \
            self.findFunction + \
            self.findOneFunction + \
            self.findByIdFunction + \
            self.findRawByIdFunction + \
            self.findCrossByIdFunction + \
            self.createOneFunction + \
            self.connectionSearchFunction + \
            '}\n\n' + \
            'export default '+tbn+';\n'

if __name__ == '__main__':
    tsc = TsClassGenerator('MarketingActivity')
    f = open('MA.ts','w')
    f.write(tsc.wholeContent)