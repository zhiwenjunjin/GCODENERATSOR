import MarketingActivityWechatGroup from './MarketingActivityWechatGroup';
import MarketingActivityWechatGroupModel, {
  IMarketingActivityWechatGroup,
} from './MarketingActivityWechatGroupModel';

import MarketingActivityWechatGroupInputType from './types/MarketingActivityWechatGroupInputType';
import MarketingActivityWechatGroupType from './types/MarketingActivityWechatGroupType';

import marketingActivityWechatGroup from './queries/MarketingActivityWechatGroup';
import marketingActivityWechatGroupsConnection from './queries/MarketingActivityWechatGroupsConnection';

import createMarketingActivityWechatGroup from './mutations/createMarketingActivityWechatGroup';
import updateMarketingActivityWechatGroup from './mutations/updateMarketingActivityWechatGroup';

export default MarketingActivityWechatGroup;
export {
  MarketingActivityWechatGroupModel,
  IMarketingActivityWechatGroup,
  MarketingActivityWechatGroupInputType,
  MarketingActivityWechatGroupType,
  marketingActivityWechatGroup,
  marketingActivityWechatGroupsConnection,
  createMarketingActivityWechatGroup,
  updateMarketingActivityWechatGroup,
};
export * from './types/MarketingActivityWechatGroupInputType';
export * from './types/MarketingActivityWechatGroupType';
