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
        

        self.className = \
            'class '+tbn+' {\n' + \
