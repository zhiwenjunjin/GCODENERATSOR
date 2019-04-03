from BasicGenerator import SimplestModel as sm
import Utilities as ut
import os
import re

def convertFn(tbn,template,export,ignore=[]):
    tbFile = open(('/Users/junjinchen/Documents/Bitbucket/rainbow-parrotfish/prisma/datamodel/%s'%tbn),'r')
    tbFileString = tbFile.read()
    isDeleted = re.findall(r'type (\w+)\s*{[^{]*?isDeleted\:\s*Boolean!? \@default\(value\: false\)',tbFileString,flags=re.DOTALL)
    # print(isDeleted,tbn)
    newFile = open('generated/%s'%export,'r')
    newString = newFile.read()
    # print('generated/%s'%export)

    for isd in isDeleted:
        newString = newString.replace('#deletable',('%s\n#deletable'%isd))

    newFile = open('generated/%s'%export,'w')
    newFile.write(newString)

def accurateConvert(tbn,template,export,ignore=[],isDeleted=[]):
    tbFile = open(('/Users/junjinchen/Documents/Bitbucket/rainbow-parrotfish/prisma/datamodel/%s'%tbn),'r')
    tbFileString = tbFile.read()
    
    current_tbns = re.findall(r'type (\w+)\s?{(.*?)}',tbFileString,flags=re.DOTALL)
    relatedProps = map((lambda (a,b):(a,re.findall(r'(\w+):\s*\[(\w+)',b,flags=re.DOTALL))),current_tbns)
    

    newFile = open('generated/%s'%export,'r')
    newString = newFile.read()

    for curr_tbn, prop_tbn in relatedProps:
        for prop, tbn in prop_tbn:
            if tbn in isDeleted:
                newString = newString.replace('#props',('%s-%s\n#props'%(curr_tbn,prop)))

    newFile = open('generated/%s'%export,'w')
    newFile.write(newString)

def readStatus(tbn,template,export,ignore=[]):
    tbFile = open(('/Users/junjinchen/Documents/Bitbucket/rainbow-parrotfish/prisma/datamodel/%s'%tbn),'r')
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
