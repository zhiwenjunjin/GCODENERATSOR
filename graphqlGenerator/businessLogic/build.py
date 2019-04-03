from BasicGenerator import SimplestModel as sm
import Utilities as ut
import os
import re
import datamodelReader as dr
import psm2blConverter as p2b
import blGen as blg
import resolverIndexGen as igen


if __name__ == '__main__':
    simplestModel = sm()

    genDir = 'generated'
    if not os.path.exists(genDir):
        os.mkdir(genDir)

    #read status
    dirName = '/Users/junjinchen/Documents/Bitbucket/rainbow-parrotfish/prisma/datamodel'
    export = ('theStatus','#switchable')

    simplestModel.convertFilesInDir(dirName,dr.readStatus,export)

    #read templates to graphql file
    qs = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blgrTemp/queryTemplate','r').read()
    ms = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blgrTemp/mutationTemplate','r').read()
    ins = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blgrTemp/inputTemplate','r').read()
    blgrs = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blgrTemp/blgrTemplate','r').read()
    stTemp = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blgrTemp/statusTemplate','r').read()

    stList = open('generated/theStatus').read().split('\n')

    ign = ['id','isDeleted','status','sort','level','createdAt','updatedAt']
    scalarTs = ['ID','String','Int','Float','Boolean','Long','BigInt','BigDecimal','DateTime','Date','Json','Binary']

    temps = [qs,ms,ins,blgrs,stTemp]

    prghDir = '/Users/junjinchen/Documents/Bitbucket/rainbow-parrotfish/prisma/datamodel'

    simplestModel.convertFilesInDir2_0(prghDir,p2b.graphql2graphqlConverter,temps,ign,scalarTs,stList)

    #graphql to resolver
    queryString = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blresolverTemp/query','r').read()
    queryGetString = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blresolverTemp/queryres-getById','r').read()
    mutationString = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blresolverTemp/mutation','r').read()
    mutationResString = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blresolverTemp/mutationres','r').read()
    mutationNonScalar = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blresolverTemp/mutationres-nonscalar','r').read()
    index = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blresolverTemp/index','r').read()
    mutationStTemp = open('/Users/junjinchen/Documents/GCODENERATSOR/graphqlGenerator/businessLogic/templates/blresolverTemp/mutationstatus').read()

    temps = [queryString,queryGetString,mutationString,mutationResString,mutationNonScalar,index,mutationStTemp]
    prghDir = 'generated/graphql'

    simplestModel.convertFilesInDir2_0(prghDir,p2b.graphql2blResolver,temps,status=stList)


    #read is-deleted
    dirName = '/Users/junjinchen/Documents/Bitbucket/rainbow-parrotfish/prisma/datamodel'
    export = ('isDeleted','#deletable')

    genDir = 'generated'
    if not os.path.exists(genDir):
        os.mkdir(genDir)
    simplestModel.convertFilesInDir(dirName,dr.convertFn,export)

    #read is deleted props
    isdFile = open('generated/isDeleted','r')
    isdList = isdFile.read().split('\n')

    export = ('isDeletedProps','#props')
    kwargs = {'isDeleted': isdList}
    simplestModel.convertFilesInDir(dirName,dr.accurateConvert,export,kwargs=kwargs)

    #update resolver files
    temp = 'templates/returnNICE'
    dirName = '/Users/junjinchen/Documents/Bitbucket/rainbow-parrotfish/src/generated/tmp-resolvers'
    ignore = ['index','Mutation','Query']
    throw_ignore = ['CountryResult','SessionTemplate','SubscribingResult']
    ignorePattern = 'Get\w+Result'

    isdProps = open('generated/isDeletedProps','r').read().split('\n')

    # simplestModel.updateFilesInDir(dirName,updateFileFn2_0,temp,ignore,isdList)
    simplestModel.updateFilesInDir2_0(dirName,blg.updateFileFn4_0,temp,ignore,isdProps,throw_ignore)
    # updateFileFn3_0('ServiceSheet',temp,ignore,isdList,throw_ignore)


    temp = 'templates/returnNICE'
    dirName = '/Users/junjinchen/Documents/Bitbucket/rainbow-parrotfish/src/generated/tmp-resolvers'
    ignore = ['index','Mutation','Query']
    ignorePattern = 'Get\w+Result'

    isdFile = open('generated/isDeleted','r')
    isdList = isdFile.read().split('\n')
    unchangedFile=['Tutor.ts','StaticAgreementCompanyEnum.ts']
    undir = '/Users/junjinchen/Documents/Bitbucket/rainbow-parrotfish/src/resolvers/SubResolver'

    simplestModel.updateFilesInDir3_0(dirName,igen.updateFileFn2_0,temp,ignore,isdList,unchanged=unchangedFile,undir=undir)