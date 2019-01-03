import Utilities as ut

class TsIndexGenerator:

    def __init__(self,tbn='TableName'):
        
        uc_tbn = ut.uncapitalize(tbn)
        self.indexFile = open('TempIndex.ts','r')
        self.content = self.indexFile.read()
        self.wholeContent = self.content.replace('[TableName]',tbn)
        self.wholeContent = self.wholeContent.replace('[tableName]',uc_tbn)

if __name__ == '__main__':

    tsid = TsIndexGenerator('MarketingActivityWechatGroup')
    f = open('MAID.ts','w')
    f.write(tsid.wholeContent)
