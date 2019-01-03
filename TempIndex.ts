import [TableName] from './[TableName]';
import [TableName]Model, {
  I[TableName],
} from './[TableName]Model';

import [TableName]InputType from './types/[TableName]InputType';
import [TableName]Type from './types/[TableName]Type';

import [tableName] from './queries/[TableName]';
import [tableName]sConnection from './queries/[TableName]sConnection';

import create[TableName] from './mutations/create[TableName]';
import update[TableName] from './mutations/update[TableName]';

export default [TableName];
export {
  [TableName]Model,
  I[TableName],
  [TableName]InputType,
  [TableName]Type,
  [tableName],
  [tableName]sConnection,
  create[TableName],
  update[TableName],
};
export * from './types/[TableName]InputType';
export * from './types/[TableName]Type';
