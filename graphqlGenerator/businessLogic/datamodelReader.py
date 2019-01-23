from BasicGenerator import SimplestModel as sm
import Utilities as ut
import os
import re

def convertFn(tbn,template,export,ignore=[]):
    tbFile = open(('/Users/junjinchen/Documents/GitHub/rainbow-parrotfish/prisma/datamodel/%s'%tbn),'r')
    tbFileString = tbFile.read()
    isDeleted = re.findall(r'type (\w+)\s*{[^{]*?isDeleted\: Boolean!? \@default\(value\: false\)',tbFileString,flags=re.DOTALL)
    # print(isDeleted,tbn)
    newFile = open('generated/%s'%export,'r')
    newString = newFile.read()
    # print('generated/%s'%export)

    for isd in isDeleted:
        newString = newString.replace('#deletable',('%s\n#deletable'%isd))

    newFile = open('generated/%s'%export,'w')
    newFile.write(newString)

def accurateConvert(tbn,template,export,ignore=[],isDeleted=[]):
    tbFile = open(('/Users/junjinchen/Documents/GitHub/rainbow-parrotfish/prisma/datamodel/%s'%tbn),'r')
    tbFileString = tbFile.read()
    
    relatedProps = re.findall(r'(\w+):\s*\[(\w+)',tbFileString)

    newFile = open('generated/%s'%export,'r')
    newString = newFile.read()

    for prop,tbn in relatedProps:
        if tbn in isDeleted:
            newString = newString.replace('#props',('%s\n#props'%prop))

    newFile = open('generated/%s'%export,'w')
    newFile.write(newString)

def readStatus(tbn,template,export,ignore=[]):
    tbFile = open(('/Users/junjinchen/Documents/GitHub/rainbow-parrotfish/prisma/datamodel/%s'%tbn),'r')
    tbFileString = tbFile.read()
    status = re.findall(r'type (\w+)\s*{[^{]*?\: StaticCommonStatusEnum',tbFileString,flags=re.DOTALL)
    # print(isDeleted,tbn)
    newFile = open('generated/%s'%export,'r')
    newString = newFile.read()
    # print('generated/%s'%export)

    for st in status:
        newString = newString.replace('#switchable',('%s\n#switchable'%st))

    newFile = open('generated/%s'%export,'w')
    newFile.write(newString)

if __name__ == '__main__':
    simplestModel = sm()
    dirName = 'datamodel'
    # export = ('isDeleted','#deletable')

    # genDir = 'generated'
    # if not os.path.exists(genDir):
    #     os.mkdir(genDir)
    # simplestModel.convertFilesInDir(dirName,convertFn,export)
    export = ('theStatus','#switchable')

    genDir = 'generated'
    if not os.path.exists(genDir):
        os.mkdir(genDir)
    simplestModel.convertFilesInDir(dirName,readStatus,export)
