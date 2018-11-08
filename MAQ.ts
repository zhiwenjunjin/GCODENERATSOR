import { GraphQLID, GraphQLNonNull, GraphQLSchema } from 'graphql';
import MarketingActivity from '../MarketingActivity';
import MarketingActivityType from '../types/MarketingActivityType';

const marketingActivity = {
  type: MarketingActivityType,
  args: {
    id: { type: new GraphQLNonNull(GraphQLID) },
  },
  resolve: (
    _: GraphQLSchema,
    { id }: { id: string },
    { viewer }: { viewer: Common.Viewer },
  ) => {
    return MarketingActivity.findById(viewer, id);
  },
};

export default marketingActivity;
