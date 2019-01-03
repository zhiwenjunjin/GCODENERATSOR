import os
import Utilities as ut
class SimplestModel:

    def generate(self, templateFileName,tbls,replaceFn,renameFn):
        templateFile = open(templateFileName,'r')
        for t in tbls:
            templateString = templateFile.read()
            newString = replaceFn(templateString,t)
            newFile = open(renameFn(t),'w')
            newFile.write(newString)

def replaceFn(temps,t):
    newString = temps
    newString = newString.replace('[tbn]',ut.lower_case(t))
    newString = newString.replace('[TBn]',t)
    newString = newString.replace('[tBn]',ut.uncapitalize(t))
    return newString

def renameFn(t):
    return ut.uncapitalize(t)+'Service.ts'

if __name__ == '__main__':
    simplestModel = SimplestModel()
    tbls = ['TableName']
    tempFile = 'Tempgraphql'
    simplestModel.generate(tempFile,tbls,replaceFn,renameFn)