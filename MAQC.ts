import { GraphQLSchema } from 'graphql';
import connectionDefault, {
  connectionCustomArgs,
  IPageArgs,
} from '../../Pagniation/types/PaginationType';
import MarketingActivity from '../MarketingActivity';
import MarketingActivitysConnectionType from '../types/MarketingActivityType';

const marketingActivityConnection = {
  type: connectionDefault(MarketingActivityType),
  args: connectionCustomArgs,
  resolve: (
    _: GraphQLSchema,
    args: IPageArgs,
    { viewer }: { viewer: Common.Viewer },
  ) {
    return MarketingActivity.connectionSearch(viewer, args);
  },
};

export default marketingActivitysConnection;
