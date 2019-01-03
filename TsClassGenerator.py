import Utilities as ut

class TsClassGenerator:

    def __init__(self,tbn='TableName'):
        
        uc_tbn = ut.uncapitalize(tbn)
        lrc_tbn = ut.lower_case(tbn)

        self.tempClass = open('TempClass.ts','r')
        self.content = self.tempClass.read()

        self.wholeContent = self.content.replace('[TableName]',tbn)
        self.wholeContent = self.wholeContent.replace('[tableName]',uc_tbn)
        self.wholeContent = self.wholeContent.replace('[tablename]',lrc_tbn)

if __name__ == '__main__':
    tsc = TsClassGenerator('MarketingActivityWechatGroup')
    f = open('MA.ts','w')
    f.write(tsc.wholeContent)