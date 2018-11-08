/* add header here */
/* add description here */
const MarketingActivityType = new GraphQLObjectType({
  name: 'MarketingActivity',
  fields: () => ({
    id: { type: new GraphQLNonNull(GraphQLID) },
    created: {
      type: new GraphQLNonNull(GraphQLString),
      resolve: ({ created }) =>
        created && typeof created !== 'string'
          ? created.toISOString()
          : created,
    },
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

/* add description here */
const MarketingActivityConnectionType = new GraphQLObjectType({
  name: 'MarketingActivityConnection',
  fields: () => ({
    id: { type: new GraphQLNonNull(GraphQLID) },
    created: {
      type: new GraphQLNonNull(GraphQLString),
      resolve: ({ created }) =>
        created && typeof created !== 'string'
          ? created.toISOString()
          : created,
    },
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

export { MarketingActivityConnectionType };
export default MarketingActivityType;
