'use strict';

module.exports = function () {
  return {
    restrict: 'E',
    scope: {
      auth: '=',
      groupsEnabled: '=',
      isSidebar: '=',
      onLogin: '&',
      onLogout: '&',
      searchController: '=',
      accountDialog: '=',
      shareDialog: '=',
      sortBy: '=',
      sortOptions: '=',
      onChangeSortBy: '&',
    },
    templateUrl: 'top_bar.html',
  };
};
