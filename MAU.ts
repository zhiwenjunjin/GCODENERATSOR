import { GraphQLID, GraphQLNonNull, GraphQLSchema } from 'graphql';

import MarketingActivity from '../../MarketingActivity';
import MarketingActivityInputType, { IMarketingActivityInputType } from '../types/MarketingActivityInputType';
import MarketingActivityType from '../types/MarketingActivityType';

const updateMarketingActivity = {
  type: MarketingActivityType,
  args: {
    id: { type: new GraphQLNonNull(GraphQLID) },
    input: { type: new GraphQLNonNull(MarketingActivityInputType) },
  },
  resolve: async (
    _: GraphQLSchema,
    { id, input }: { id: string; input: IMarketingActivityInputType },
    { viewer }: { viewer: Common.Viewer },
  ) => {
    return MarketingActivity.updateById(viewer, id, input);
  },
};

export default updateMarketingActivity;
