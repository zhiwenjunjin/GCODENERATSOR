import * as mongoose from 'mongoose';

interface IMarketingActivity {
  id: string;
  created: Date;
  title: string;
  person: string;
}

interface IMarketingActivityDocument 
  extends mongoose.Document,
    IMarketingActivity {
  id: string;
  toJSON(): IMarketingActivity;
} 

const marketingActivitySchema = new mongoose.Schema(
  {    created: { type: Date, default: Date.now },
    title: { type: String },
    person: { type: String },
  },
  {
    collection: 'marketingActivitys',
  },
);

const MarketingActivityModel = mongoose.model<IMarketingActivityDocument>(
  'MarketingActivity',
  marketingActivitySchema,
);

export default MarketingActivityModel;
export { IMarketingActivity };
