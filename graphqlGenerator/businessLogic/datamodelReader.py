from BasicGenerator import SimplestModel as sm
import Utilities as ut
import os
import re

def convertFn(tbn,template,ignore=[]):
    tbFile = open(('datamodel/%s'%tbn),'r')
    tbFileString = tbFile.read()
    isDeleted = re.findall(r'type (\w+)\s*{.*?isDeleted\: Boolean \@default\(value\: false\)',tbFileString,flags=re.DOTALL)
    print(isDeleted,"fucking deleted!")
    newFile = open('generated/isDeleted','r')
    newString = newFile.read()

    for isd in isDeleted:
        newString = newString.replace('#deletable',('%s\n#deletable'%isd))

    newFile = open('generated/isDeleted','w')
    newFile.write(newString)

if __name__ == '__main__':
    simplestModel = sm()
    dirName = 'datamodel'
    simplestModel.convertFilesInDir(dirName,convertFn)
