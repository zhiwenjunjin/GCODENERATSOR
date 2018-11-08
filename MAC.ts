import { GraphQLNonNull, GraphQLSchema } from 'graphql';
import MarketingActivity from '../MarketingActivity';
import MarketingActivitysInputType, {
  IMarketingActivityInputType,
} from '../types/MarketingActivityInputType';
import MarketingActivityType from '../types/MarketingActivityType';

const createMarketingActivity = {
  type: MarketingActivityType,
  args: {
    input: { type: new GraphQLNonNull(MarketingActivityInputType) },
  },
  resolve: async (
    _: GraphQLSchema,
    { input }: { input: IMarketingActivityInputType },
    { viewer }: { viewer: Common.Viewer },
  ) => {
    return MarketingActivity.createOne(viewer, input);
  },
};

export default createMarketingActivity;
