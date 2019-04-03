from BasicGenerator import SimplestModel as sm
import Utilities as ut
import os
import re

def replaceFn(temps,secondTemp,tbls):
    newString = temps
    print('fuck'+newString)
    for t in tbls:
        tempString = secondTemp.replace('[TBn]',t).replace('[tBn]',ut.uncapitalize(t))
        newString = newString.replace('// NEW FUNCTION','%s\n// NEW FUNCTION' % tempString)
    return newString

def inputReplacefn(temp1,temp2,tbls):
    newString = temp1
    for t in tbls:
        tempString = temp2.replace('[TBn]',t)
        newString = newString.replace('#INPUT HERE','%s\n#INPUT HERE' % tempString)
    return newString

def updateFileFn(tbn,template,ignore=[]):
    if(tbn not in ignore):
        tbFile = open(('SubResolver/%s.ts'%tbn),'r')
        tbFileString = tbFile.read()
        tbFileString = tbFileString.replace('\'../generated/graphqlgen','\'../../generated/graphqlgen')
        # props = re.findall(r'\w+: \(p',tbFileString)
        # tempFile = open(template,'r')
        # tempString = tempFile.read()
        # uc_tbn = ut.uncapitalize(re.sub('(?P<tbn>\w+)Connection','\g<tbn>sConnection',tbn))
        # print(props)
        # for p in props:
        #     p = p.split(':')[0]
        #     newString = tempString.replace('[tbn]',uc_tbn).replace('[propn]',p)
        #     tbFileString = tbFileString.replace("throw new Error('Resolver not implemented');",newString,1)
        tbFile = open(('SubResolver/%s.ts'%tbn),'w')
        tbFile.write(tbFileString)

def updateFileFn2_0(tbn,template,ignore=[],isDeleted=[]):
    if(tbn in ignore):
        tbFile = open(('/Users/junjinchen/Documents/Bitbucket/rainbow-parrotfish/src/generated/tmp-resolvers/%s.ts'%tbn),'r')
        tbFileString = tbFile.read()
        tbFileString = tbFileString.replace('\'../graphqlgen','\'../generated/graphqlgen')
        tbFileString = tbFileString.replace('\'./','\'./SubResolver/')
        tbFileString = tbFileString.replace('SubResolver/Mutation\'','Mutation\'')
        tbFileString = tbFileString.replace('SubResolver/Query\'','Query\'')
        
        genDir = 'generated/Resolver'
        if not os.path.exists(genDir):
            os.mkdir(genDir)
        tbFile = open(('%s/%s.ts'%(genDir,tbn)),'w')
        tbFile.write(tbFileString)


if __name__ == '__main__':
    simplestModel = sm()
    tbls = ['JobIntention','EducationExperience','WorkExperience','ProjectExperience','SchoolExperience','LanguageSkill','JobSkill','Certificate','Award','SocialHomepage']
    temp1 = 'templates/blStudentTemplate'
    # temp2 = 'templates/resolverDeleteTemplate'
    temp2 = 'templates/cvDeleteTemplate'
    # temp2 = 'templates/studentCreateTemplate'
    # temp2 = 'templates/blInnerTemplate'
    # simplestModel.generateComplex(temp1,temp2,tbls,replaceFn)
    # inputTemp = 'templates/inputTemp'
    # inputBasicTemp = 'templates/inputbasictemp'
    # simplestModel.generateComplex(inputBasicTemp,inputTemp,tbls,inputReplacefn)

    temp = 'templates/returnNICE'
    dirName = 'tmp-resolvers'
    ignore = ['index','Mutation','Query']
    ignorePattern = 'Get\w+Result'

    isdFile = open('generated/isDeleted','r')
    isdList = isdFile.read().split('\n')

    simplestModel.updateFilesInDir(dirName,updateFileFn2_0,temp,ignore,isdList)