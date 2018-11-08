/* add headers here */
class MarketingActivity {
  public static async find(_: Common.Viewer, args: object) {
    return MarketingActivityModel.find(args);
  }
  public statci async findOne(_: Common.Viewer, args: object) {
    return MarketingActivityModel.findOne(args);
  }
  public static async findById(
    _: Common.Viewer,
    id: string | mongoose.Types.ObjectId,
  ) {
    return MarketingActivityModel.findById(id);
  }
  public static async findRawById(id: string | mongoose.Types.ObjectId) {
    const marketingActivity = await MarketingActivityModel.findById(id, '-__v');
    if (!marketingActivity) {
      throw new Error(/*add error message here*/);
    }
    const marketingActivityJson = {
      ...omit(MarketingActivity.toJSON(), '_id'),
      id: marketingActivity.id,
    };
    return marketingActivityJson;
  }
  public static async findCrossById(id: string | mongoose.Types.ObjectId) {
    const marketingActivityJson = await this.findRawById(id);
    return {
      ...marketingActivityJson,
    };
  }

  public static async createOne(
    viewer: Common.Viewer,
    input: IMarketingActivityInputType,
  ) {
    if (!viewer) {
      throw new Error('Unauthorized');
    }
    try {
      /* add restriction here */
      const marketingActivityDoc = new MarketingActivityModel({
        ...input,
      });
      try { 
        const marketingActivity = await marketingActivityDoc.save();
        await elasticCreateCross('marketingactivity', marketingActivityDoc.id);
        return marketingActivity;
      } catch (e) {
         throw e;
      }
    } catch(e) {
       throw e;
    }
  }

  public static async connectionSearch(
    viewer: Common.Viewer,
    args: Common.PageArgs,
  ) {
    const newArgs = formatArgs(args);
    const data = await connectionSearch(newArgs, {
      index: 'marketingactivity',
      type: 'marketingactivity',
    });
    return data;
  }
}

export default MarketingActivity;
