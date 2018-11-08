/* add header here */
interface IMarketingActivityInputType {
  title: string;
  person: string;
}

/* add descriptions here */
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
