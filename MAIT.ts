import {
  GraphQLInputObjectType,
  GraphQLString,
} from 'graphql';
/* not add header here */

interface IMarketingActivityInputType {
  title: string;
  person: string;
}

/* not add descriptions here */
const MarketingActivityInputType = new GraphQLInputObjectType({
  name: 'MarketingActivityInput',
  fields: () => ({
    title: {
      type: GraphQLString,
      description: '',
    },
    person: {
      type: GraphQLString,
      description: '',
    },
  }),
});

export default MarketingActivityInputType;
export { IMarketingActivityInputType };
