import { GraphQLID, GraphQLNonNull, GraphQLSchema } from 'graphql';

import [TableName] from '../../[TableName]';
import [TableName]InputType, { I[TableName]InputType } from '../types/[TableName]InputType';
import [TableName]Type from '../types/[TableName]Type';

const update[TableName] = {
  type: [TableName]Type,
  args: {
    id: { type: new GraphQLNonNull(GraphQLID) },
    input: { type: new GraphQLNonNull([TableName]InputType) },
  },
  resolve: async (
    _: GraphQLSchema,
    { id, input }: { id: string; input: I[TableName]InputType },
    { viewer }: { viewer: Common.Viewer },
  ) => {
    return [TableName].updateById(viewer, id, input);
  },
};

export default update[TableName];
