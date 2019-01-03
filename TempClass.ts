/* add headers here */
import { omit } from 'lodash';
import * as mongoose from 'mongoose';
import {
  connectionSearch,
  elasticCreateCross,
  elasticUpdateCross,
} from '../ElasticSearch';
import { formatArgs } from '../Pagination/types/PaginationType';
import [TableName]Model from './[TableName]Model';
import { I[TableName]InputType } from './types/[TableName]InputType';

class [TableName] {
  public static async find(_: Common.Viewer, args: object) {
    return [TableName]Model.find(args);
  }
  public static async findOne(_: Common.Viewer, args: object) {
    return [TableName]Model.findOne(args);
  }
  public static async findById(
    _: Common.Viewer,
    id: string | mongoose.Types.ObjectId,
  ) {
    return [TableName]Model.findById(id);
  }
  public static async findRawById(id: string | mongoose.Types.ObjectId) {
    const [tableName] = await [TableName]Model.findById(id, '-__v');
    if (![tableName]) {
      throw new Error(/*add error message here*/);
    }
    const [tableName]Json = {
      ...omit([tableName].toJSON(), '_id'),
      id: [tableName].id,
    };
    return [tableName]Json;
  }
  public static async findCrossById(id: string | mongoose.Types.ObjectId) {
    const [tableName]Json = await this.findRawById(id);
    return {
      ...[tableName]Json,
    };
  }

  public static async createOne(
    viewer: Common.Viewer,
    input: I[TableName]InputType,
  ) {
    if (!viewer) {
      throw new Error('Unauthorized');
    }
    try {
      /* add restriction here */
      const [tableName]Doc = new [TableName]Model({
        ...input,
      });
      try {
        const [tableName] = await [tableName]Doc.save();
        await elasticCreateCross('[tablename]', [tableName]Doc.id);
        return [tableName];
      } catch (e) {
         throw e;
      }
    } catch (e) {
       throw e;
    }
  }

  public static async updateById(
    viewer: Common.Viewer,
    id: string | mongoose.Types.ObjectId,
    [tableName]Input: I[TableName]InputType,
  ) {
    const [tableName] = await [TableName]Model.findByIdAndUpdate(
      id,
      { $set: [tableName]Input },
      { new: true },
    );
    await elasticUpdateCross('[tablename]', id);
    return [tableName];
  }

  public static async connectionSearch(
    viewer: Common.Viewer,
    args: Common.PageArgs,
  ) {
    const newArgs = formatArgs(args);
    const data = await connectionSearch(newArgs, {
      index: '[tablename]',
      type: '[tablename]',
    });
    return data;
  }
}

export default [TableName];
