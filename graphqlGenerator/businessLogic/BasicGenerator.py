import os
class SimplestModel:

    def generate(self, templateFileName,tbls,replaceFn,renameFn):
        for t in tbls:
            templateFile = open(templateFileName,'r')
            templateString = templateFile.read()
            newString = replaceFn(templateString,t)
            newFile = open(renameFn(t),'w')
            newFile.write(newString)

    def generateSingle(self,temp,tbls,replaceFn):
        tempfile = open(temp,'r')
        tempString = tempfile.read()
        newString = replaceFn(tempString,tbls)
        indexFile = open('index.ts','w')
        indexFile.write(newString)

    def generateComplex(self,temp1,temp2,tbls,replaceFn,filename='generated/generated'):
        temp1file = open(temp1,'r')
        temp1String = temp1file.read()
        temp2file = open(temp2,'r')
        temp2String = temp2file.read()
        newString = replaceFn(temp1String,temp2String,tbls)
        newFile = open(filename,'w')
        newFile.write(newString)

    def updateFilesInDir(self,dirName,replaceFn,temps=[],ignore=[],isDeleted=[]):
        for fn in os.listdir(dirName):
            replaceFn(fn.split('.')[0],temps,ignore,isDeleted)
    def updateFilesInDir3_0(self,dirName,replaceFn,temps=[],ignore=[],isDeleted=[],unchanged=[],undir=''):
        for fn in os.listdir(dirName):
            if fn not in unchanged:
                replaceFn(fn.split('.')[0],temps,ignore,isDeleted)
            else:
                unchangedString = open('%s/%s'%(undir,fn),'r').read()
                genDir = 'generated/SubResolver'
                if not os.path.exists(genDir):
                    os.mkdir(genDir)
                open(('%s/%s'%(genDir,fn)),'w').write(unchangedString)
    def updateFilesInDir2_0(self,dirName,replaceFn,temps=[],ignore=[],isDeleted=[],throw_ignore=[]):
        for fn in os.listdir(dirName):
            replaceFn(fn.split('.')[0],temps,ignore,isDeleted,throw_ignore)

    def convertFilesInDir(self,dirName,convertFn,export,temps=[],ignore=[],kwargs={}):
        efn,ini = export
        f = open('generated/%s'%efn,'w')
        f.write(ini)
        f.close()
        for fn in os.listdir(dirName):
            convertFn(fn,temps,efn,ignore,**kwargs)

    def convertFilesInDir2_0(self,dirName,convertFn,temps=[],ignore=[],scalarTypes=[],status=[]):
        for fn in os.listdir(dirName):
            convertFn(('%s/%s'%(dirName,fn)),temps,ignore,scalarTypes,status)

    def convertFilesInDir3_0(self,dirName,convertFn,temps=[],args=[]):
        for fn in os.listdir(dirName):
            convertFn(('%s/%s'%(dirName,fn)),temps,args)