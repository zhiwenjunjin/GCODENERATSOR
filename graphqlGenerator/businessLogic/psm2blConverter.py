from BasicGenerator import SimplestModel as sm
import Utilities as ut
import os
import re

def graphql2graphqlConverter(pgname,templateStrings=[],ignoreProps=[],scalarTypes=[],status=[]):
    #read the prisma graphql file
    pgrph = open(pgname,'r')
    pgrghString = pgrph.read()
    # if pgname == '/Users/junjinchen/Documents/Bitbucket/rainbow-parrotfish/prisma/datamodel/course.graphql':
    #     print (pgrghString)
    #get the types
    toTuple = map((lambda (a,b):(a,re.findall(r'(\s{2}?"""[^[]*?""")?\n\s*(\w+):\s*([A-Z]\w+)(!*)',b,flags=re.DOTALL)) ),re.findall(r'type\s+(\w+)\s*{(.*?)}',pgrghString,flags=re.DOTALL))
    #read templates
    queryString = templateStrings[0]
    mutationString = templateStrings[1]
    inputString = templateStrings[2]
    blgrString = templateStrings[3]
    statusString = ''
    if(len(templateStrings)>=5):
        statusString = templateStrings[4]
    #convert to Query and Mutation
    for t, pl in toTuple:
        #query string
        newqueryString = queryString.replace('[TBn]',t)
        newqueryString = newqueryString.replace('[s]','es'if ut.check_end_with_s(t) else '<-ies' if ut.check_end_with_y(t) and not ut.check_sec_last_end_with_a(t) else 's').replace('y<-','')
        blgrString = blgrString.replace('#query',('%s\n#query'%newqueryString))
        #mutation string
        newMutationString = mutationString.replace('[TBn]',t)
        blgrString = blgrString.replace('#mutation',('%s\n\n#mutation'%newMutationString))
        #status string
        if t in status:
            newStatusString = statusString.replace('[TBn]',t)
            blgrString = blgrString.replace('#mutation',('%s\n\n#mutation'%newStatusString))

        newInputString = inputString.replace('[TBn]',t)
        newInputString = newInputString.replace('[s]','es'if ut.check_end_with_s(t) else '<-ies' if ut.check_end_with_y(t) and not ut.check_sec_last_end_with_a(t) else 's').replace('y<-','')
        for st,p,pt,q in pl:
            if p not in ignoreProps:
                if pt in scalarTypes:
                    # print(st)
                    newInputString = newInputString.replace('#updateproperty','%s\n  %s: %s\n#updateproperty'%(st,p,pt))
                    newInputString = newInputString.replace('#createproperty','%s\n  %s: %s%s\n#createproperty'%(st,p,pt,q))
                else:
                    newInputString = newInputString.replace('#updateproperty','%s\n  %sId: String\n#updateproperty'%(st,p))
                    newInputString = newInputString.replace('#createproperty','%s\n  %sId: String%s\n#createproperty'%(st,p,q))
        blgrString = blgrString.replace('#input','%s\n\n#input'%newInputString)
    #write to blgraph
    pureFileName = re.findall(r'.*\/(.+)',pgname)[0]
    genDir = 'generated/graphql'
    if not os.path.exists(genDir):
        os.mkdir(genDir)
    blgrph = open(('%s/%s'%(genDir,pureFileName)),'w')
    blgrph.write(blgrString)

def graphql2blResolver(blgname,templateStrings=[],ignoreProps=[],args=[],status=[]):
    #read the business logic graphql file
    blgrph = open(blgname,'r')
    blgrphString = blgrph.read()
    #get the module name
    modn = re.findall(r'.*\/(\w+)',blgname)[0]
    #get the function name, table name, function type-query
    qs=re.findall(r'Query\s*{(.*?)}',blgrphString,re.DOTALL)[0]
    #example qs ['LanguageSkill', 'JobSkill', 'Certificate', 'ProjectExperience', 'SchoolExperience', 'Award', 'SocialHomepage', 'JobIntention', 'Student', 'CV']
    qt=re.findall(r'get(\w+)ById\(.*?\)\:',qs)
    #for mutation
    mt=map(lambda (a,b): (a,re.findall(r'(\w+)Id: String',b)),re.findall(r'input (\w+)UpdateInput\s*{(.*?)}',blgrphString,re.DOTALL))
    #read templates
    queryString = templateStrings[0]
    queryGetByIdString = templateStrings[1]
    mutationString = templateStrings[2]
    mutationResString = templateStrings[3]
    mutationNonScalar = templateStrings[4]
    index = templateStrings[5]

    statusString = templateStrings[6] if len(templateStrings) > 6 else ''

    #convert to service-query
    for qtbn in qt:
        newQGetString = queryGetByIdString.replace('[TBn]',qtbn).replace('[tBn]',ut.uncapitalize(qtbn)).replace('[modn]',modn)
        newQGetString = newQGetString.replace('[s]','es'if ut.check_end_with_s(qtbn) else '<-ies' if ut.check_end_with_y(qtbn) and not ut.check_sec_last_end_with_a(qtbn) else 's').replace('y<-','')
        queryString = queryString.replace('//query resolvers','%s\n//query resolvers'%newQGetString)
        queryString = queryString.replace('/*whereInput*/','%sWhereInput, /*whereInput*/'%qtbn)
    queryString = queryString.replace('[modn]',modn)
    #convert to service-mution
    for mtbn, nonScalarlist in mt:
        newMResString = mutationResString.replace('[modn]',modn).replace('[TBn]',mtbn)
        for ns in nonScalarlist:
            newNonString = mutationNonScalar.replace('[nonscalar]',ns)
            newMResString = newMResString.replace('/*non-scalar*/','%sId, /*non-scalar*/'%ns).replace('//nonscalar2id','%s\n//nonscalar2id'%newNonString)
        mutationString = mutationString.replace('//resolvers','%s\n//resolvers'%newMResString)
        mutationString = mutationString.replace('/*updateinput*/','%sUpdateInput,/*updateinput*/'%mtbn)
        if mtbn in status:
            newStatusString = statusString.replace('[modn]',modn).replace('[TBn]',mtbn)
            mutationString = mutationString.replace('//resolvers','%s\n//resolvers'%newStatusString)
    mutationString = mutationString.replace('[modn]',modn)

    index = index.replace('[modn]',modn)
    #write to service
    outterDir = 'generated/service'
    if not os.path.exists(outterDir):
        os.mkdir(outterDir)
    genDir = 'generated/service/%s'%ut.capitalize(modn)
    if not os.path.exists(genDir):
        os.mkdir(genDir)
    queryFile = open('%s/query.ts'%genDir,'w')
    queryFile.write(queryString)
    mutationFile = open('%s/mutation.ts'%genDir,'w')
    mutationFile.write(mutationString)

    indexFile = open('%s/index.ts'%genDir,'w')
    indexFile.write(index)

if __name__ == '__main__':
    simplestModel = sm()

    #read templates to graphql file
    qs = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blgrTemp/queryTemplate','r').read()
    ms = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blgrTemp/mutationTemplate','r').read()
    ins = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blgrTemp/inputTemplate','r').read()
    blgrs = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blgrTemp/blgrTemplate','r').read()

    ign = ['id','isDeleted']
    scalarTs = ['ID','String','Int','Float','Boolean','Long','BigInt','BigDecimal','DateTime','Date','Json','Binary']

    temps = [qs,ms,ins,blgrs]

    prghDir = 'datamodel'

    simplestModel.convertFilesInDir2_0(prghDir,graphql2graphqlConverter,temps,ign,scalarTs)

    #graphql to resolver
    queryString = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blresolverTemp/query','r').read()
    queryGetString = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blresolverTemp/queryres-getById','r').read()
    mutationString = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blresolverTemp/mutation','r').read()
    mutationResString = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blresolverTemp/mutationres','r').read()
    mutationNonScalar = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blresolverTemp/mutationres-nonscalar','r').read()
    index = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blresolverTemp/index','r').read()
    # queryListString = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blresolverTemp/queryres-list','r').read()
    # queryListWPString = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blresolverTemp/queryres-list-conn','r').read()

    temps = [queryString,queryGetString,mutationString,mutationResString,mutationNonScalar,index]
    prghDir = 'generated/graphql'

    simplestModel.convertFilesInDir2_0(prghDir,graphql2blResolver,temps)