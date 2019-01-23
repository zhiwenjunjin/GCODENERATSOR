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
    if(tbn not in ignore):
        tbFile = open(('tmp-resolvers/%s.ts'%tbn),'r')
        tbFileString = tbFile.read()
        tbFileString = tbFileString.replace('\'../graphqlgen','\'../../generated/graphqlgen')
        props = re.findall(r'\w+: \(p',tbFileString)
        tempFile = open(template,'r')
        tempString = tempFile.read()
        uc_tbn = ut.uncapitalize(re.sub('(?P<tbn>\w+)Connection','\g<tbn>sConnection',tbn))
        
        for p in props:
            p = p.split(':')[0]
            # print(ut.capitalize(p)[:-1],ut.capitalize(p)[:-1] in isDeleted)
            newString = ''
            if(p=='aggregate'):
                newString = tempString.replace('[tbn]','%s()'%uc_tbn).replace('[propn]',('%s()'%p))
            elif(ut.capitalize(p)[:-1] in isDeleted):
                newString = tempString.replace('[tbn]','%s({ id: parent.id })'%uc_tbn).replace('[propn]',('%s({ where: { isDeleted: false } })'%p))
            else:
                newString = tempString.replace('[tbn]','%s({ id: parent.id })'%uc_tbn).replace('[propn]',('%s()'%p))
            tbFileString = tbFileString.replace("throw new Error('Resolver not implemented');",newString,1)
        

        genDir = 'SubResolver'
        if not os.path.exists(genDir):
            os.mkdir(genDir)
        tbFile = open(('%s/%s.ts'%(genDir,tbn)),'w')
        tbFile.write(tbFileString)

def updateFileFn3_0(tbn,template,ignore=[],isDeleted=[],throw_ignore=[]):
    if(tbn not in ignore):
        tbFile = open(('/Users/junjinchen/Documents/GitHub/rainbow-parrotfish/src/generated/tmp-resolvers/%s.ts'%tbn),'r')
        tbFileString = tbFile.read()
        tbFileString = tbFileString.replace('\'../graphqlgen','\'../../generated/graphqlgen')
        props = re.findall(r'\w+: \(p',tbFileString)
        tempFile = open(template,'r')
        tempString = tempFile.read()
        rawConnTbn = re.findall(r'(\w+)Connection',tbn)
        uc_tbn = ''
        if rawConnTbn:
            rawConnTbn = rawConnTbn[0]
            # print('fucking',rawConnTbn,'%se'%rawConnTbn if ut.check_end_with_s(rawConnTbn) else ('%s<-ie'%rawConnTbn if ut.check_end_with_y(rawConnTbn) and not ut.check_sec_last_end_with_a(rawConnTbn) else rawConnTbn))
            uc_tbn = ut.uncapitalize('%ssConnection'%('%se'%rawConnTbn if ut.check_end_with_s(rawConnTbn) else ('%s<-ie'%rawConnTbn if ut.check_end_with_y(rawConnTbn) and not ut.check_sec_last_end_with_a(rawConnTbn) else rawConnTbn))).replace('y<-','')
        else:
            uc_tbn = ut.uncapitalize(tbn)
        
        # print(tbn,throw_ignore,props)
        if tbn not in throw_ignore:
            for p in props:
                p = p.split(':')[0]
                # print(ut.capitalize(p), ut.capitalize(p) in isDeleted)
                newString = ''
                if(p=='aggregate'):
                    newString = tempString.replace('[tbn]','%s()'%uc_tbn).replace('[propn]',('%s()'%p))
                elif(ut.capitalize(p)[:-1] in isDeleted):
                    newString = tempString.replace('[tbn]','%s({ id: parent.id })'%uc_tbn).replace('[propn]',('%s({ where: { isDeleted: false } })'%p))
                else:
                    newString = tempString.replace('[tbn]','%s({ id: parent.id })'%uc_tbn).replace('[propn]',('%s()'%p))
                tbFileString = tbFileString.replace("throw new Error('Resolver not implemented')",newString,1)

        genDir = 'generated/SubResolver'
        if not os.path.exists(genDir):
            os.mkdir(genDir)
        tbFile = open(('%s/%s.ts'%(genDir,tbn)),'w')
        tbFile.write(tbFileString)

def updateFileFn4_0(tbn,template,ignore=[],isDeletedProps=[],throw_ignore=[]):
    if(tbn not in ignore):
        tbFile = open(('/Users/junjinchen/Documents/GitHub/rainbow-parrotfish/src/generated/tmp-resolvers/%s.ts'%tbn),'r')
        tbFileString = tbFile.read()
        tbFileString = tbFileString.replace('\'../graphqlgen','\'../../generated/graphqlgen')
        props = re.findall(r'\w+: \(p',tbFileString)
        tempFile = open(template,'r')
        tempString = tempFile.read()
        rawConnTbn = re.findall(r'(\w+)Connection',tbn)
        uc_tbn = ''
        if rawConnTbn:
            rawConnTbn = rawConnTbn[0]
            # print('fucking',rawConnTbn,'%se'%rawConnTbn if ut.check_end_with_s(rawConnTbn) else ('%s<-ie'%rawConnTbn if ut.check_end_with_y(rawConnTbn) and not ut.check_sec_last_end_with_a(rawConnTbn) else rawConnTbn))
            uc_tbn = ut.uncapitalize('%ssConnection'%('%se'%rawConnTbn if ut.check_end_with_s(rawConnTbn) else ('%s<-ie'%rawConnTbn if ut.check_end_with_y(rawConnTbn) and not ut.check_sec_last_end_with_a(rawConnTbn) else rawConnTbn))).replace('y<-','')
        else:
            uc_tbn = ut.uncapitalize(tbn)
        
        # print(tbn,throw_ignore,props)
        if tbn not in throw_ignore:
            for p in props:
                p = p.split(':')[0]
                # print(ut.capitalize(p), ut.capitalize(p) in isDeleted)
                newString = ''
                if(p=='aggregate'):
                    newString = tempString.replace('[tbn]','%s()'%uc_tbn).replace('[propn]',('%s()'%p))
                elif(p in isDeletedProps):
                    newString = tempString.replace('[tbn]','%s({ id: parent.id })'%uc_tbn).replace('[propn]',('%s({ where: { isDeleted: false } })'%p))
                else:
                    newString = tempString.replace('[tbn]','%s({ id: parent.id })'%uc_tbn).replace('[propn]',('%s()'%p))
                tbFileString = tbFileString.replace("throw new Error('Resolver not implemented')",newString,1)

        genDir = 'generated/SubResolver'
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
    throw_ignore = ['CountryResult','SessionTemplate']
    ignorePattern = 'Get\w+Result'

    isdFile = open('generated/isDeleted','r')
    isdList = isdFile.read().split('\n')

    # simplestModel.updateFilesInDir(dirName,updateFileFn2_0,temp,ignore,isdList)
    simplestModel.updateFilesInDir2_0(dirName,updateFileFn3_0,temp,ignore,isdList,throw_ignore)
    # updateFileFn3_0('ServiceSheet',temp,ignore,isdList,throw_ignore)