/* add headers here */
import { omit } from 'lodash';
import * as mongoose from 'mongoose';
import {
  connectionSearch,
  elasticCreateCross,
  elasticUpdateCross,
} from '../ElasticSearch';
import { formatArgs } from '../Pagination/types/PaginationType';
import MarketingActivityWechatGroupModel from './MarketingActivityWechatGroupModel';
import { IMarketingActivityWechatGroupInputType } from './types/MarketingActivityWechatGroupInputType';

class MarketingActivityWechatGroup {
  public static async find(_: Common.Viewer, args: object) {
    return MarketingActivityWechatGroupModel.find(args);
  }
  public static async findOne(_: Common.Viewer, args: object) {
    return MarketingActivityWechatGroupModel.findOne(args);
  }
  public static async findById(
    _: Common.Viewer,
    id: string | mongoose.Types.ObjectId,
  ) {
    return MarketingActivityWechatGroupModel.findById(id);
  }
  public static async findRawById(id: string | mongoose.Types.ObjectId) {
    const marketingActivityWechatGroup = await MarketingActivityWechatGroupModel.findById(id, '-__v');
    if (!marketingActivityWechatGroup) {
      throw new Error(/*add error message here*/);
    }
    const marketingActivityWechatGroupJson = {
      ...omit(marketingActivityWechatGroup.toJSON(), '_id'),
      id: marketingActivityWechatGroup.id,
    };
    return marketingActivityWechatGroupJson;
  }
  public static async findCrossById(id: string | mongoose.Types.ObjectId) {
    const marketingActivityWechatGroupJson = await this.findRawById(id);
    return {
      ...marketingActivityWechatGroupJson,
    };
  }

  public static async createOne(
    viewer: Common.Viewer,
    input: IMarketingActivityWechatGroupInputType,
  ) {
    if (!viewer) {
      throw new Error('Unauthorized');
    }
    try {
      /* add restriction here */
      const marketingActivityWechatGroupDoc = new MarketingActivityWechatGroupModel({
        ...input,
      });
      try {
        const marketingActivityWechatGroup = await marketingActivityWechatGroupDoc.save();
        await elasticCreateCross('marketingactivitywechatgroup', marketingActivityWechatGroupDoc.id);
        return marketingActivityWechatGroup;
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
    marketingActivityWechatGroupInput: IMarketingActivityWechatGroupInputType,
  ) {
    const marketingActivityWechatGroup = await MarketingActivityWechatGroupModel.findByIdAndUpdate(
      id,
      { $set: marketingActivityWechatGroupInput },
      { new: true },
    );
    await elasticUpdateCross('marketingactivitywechatgroup', id);
    return marketingActivityWechatGroup;
  }

  public static async connectionSearch(
    viewer: Common.Viewer,
    args: Common.PageArgs,
  ) {
    const newArgs = formatArgs(args);
    const data = await connectionSearch(newArgs, {
      index: 'marketingactivitywechatgroup',
      type: 'marketingactivitywechatgroup',
    });
    return data;
  }
}

export default MarketingActivityWechatGroup;
