from BasicGenerator import SimplestModel as sm
import Utilities as ut
import os
import re

def graphql2sqlCreate(pgname,sqltemp,args):
    #read from graphql
    pgrph = open(pgname,'r')
    pgrphString = pgrph.read()
    toTuple = map((lambda (a,b):(a,re.findall(r'(\w+):\s*(\[?[A-Z]\w+\!?\]?)(!*)',b)) ),re.findall(r'type\s+(\w+) {(.*?)}',pgrphString,flags=re.DOTALL))
    #open sql generated and append
    sqlFile = open(args['sqlDir'],'a+')
    #convert
    for t,pl in toTuple:
        #read temp
        sqlcreate = sqltemp[0]
        sqlcreate = sqlcreate.replace('[TBn]',t)
        for p,pt,q in pl:
            sqlcreate = sqlcreate.replace('//props','%s %s%s\n//props'%(p,pt,q))
        sqlFile.write(sqlcreate)
    sqlFile.close()


if __name__ == '__main__':
    simplestModel = sm()

    prghDir = 'datamodel'
    queryString = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/sqlCreateTemp/sqlCreate','r').read()
    args = {
        'sqlDir': 'generated/sqlCreate'
    }

    simplestModel.convertFilesInDir3_0(prghDir,graphql2sqlCreate,[queryString],args)