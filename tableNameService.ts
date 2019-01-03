/**
 * cv tablename
 */

import {TableNameCreateInput, TableNameUpdateInput, TableNameWhereUniqueInput, prisma} from '../../../src/generated/prisma-client';

const tableName:any = {};

tableName.append = async (
    data: TableNameCreateInput
) => {
    return prisma.createTableName(data);
}
tableName.update = async (
    data: TableNameUpdateInput,
    where: TableNameWhereUniqueInput
) => {
    return prisma.updateTableName({data,where});
}
tableName.delete = async (
    where: TableNameWhereUniqueInput
) => {
    const data: TableNameUpdateInput = {
        isDeleted: true
    }

    return prisma.updateTableName({data,where});
}


export {tableName};