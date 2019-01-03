class TsUpdateGenerator:

    def __init__(self,tbn='TableName'):
        self.readf = open('updateTBNTemplate.ts','r')
        self.content = self.readf.read()
        self.wholeContent = self.content.replace('[TableName]',tbn)

if __name__ == '__main__':
    tsu = TsUpdateGenerator('MarketingActivity')
    f = open('MAU.ts','w')
    f.write(tsu.wholeContent)