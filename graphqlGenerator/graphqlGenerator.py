import os
import Utilities as ut
class SimplestModel:

    def generate(self, templateFileName,tbls,replaceFn,renameFn):
        for t in tbls:
            templateFile = open(templateFileName,'r')
            templateString = templateFile.read()
            newString = replaceFn(templateString,t)
            newFile = open(renameFn(t),'w')
            newFile.write(newString)

    def generate_index(self,temp,tbls,replaceFn):
        tempfile = open(temp,'r')
        tempString = tempfile.read()
        newString = replaceFn(tempString,tbls)
        indexFile = open('index.ts','w')
        indexFile.write(newString)

def replaceFn(temps,t):
    newString = temps
    newString = newString.replace('[tbn]',ut.lower_case(t))
    newString = newString.replace('[TBn]',t)
    newString = newString.replace('[tBn]',ut.uncapitalize(t))
    return newString

def renameFn(t):
    return ('generated/%sService.ts' % ut.uncapitalize(t))

def indexReplaceFn(temps, tbls):
    newString = temps
    for t in tbls:
        uc_t = ut.uncapitalize(t)
        newString = newString.replace('// IMPORT',"import {%s} from './%sService';\n// IMPORT" % (uc_t,uc_t))
        newString = newString.replace('// EXPORT','    %s,\n// EXPORT' % (uc_t,))
        # print(newString)
    return newString

if __name__ == '__main__':
    simplestModel = SimplestModel()
    tbls = ['JobIntention','EducationExperience','WorkExperience','ProjectExperience','SchoolExperience','LanguageSkill','JobSkill','Certificate','Award','SocialHomepage']
    tempFile = 'template'
    simplestModel.generate(tempFile,tbls,replaceFn,renameFn)
    # indexTemp = 'indexTemplate'
    # simplestModel.generate_index(indexTemp,tbls,indexReplaceFn)