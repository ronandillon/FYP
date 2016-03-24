Quotr.factory('History', ['$rootScope',function($scope,$http) {

    //$("#searchText").hide();

	return{

		showhistory: function(uuid){

			url="http://52.30.239.185/history/'"+uuid+"'";


		    $.get(url, function(data){
				hist=JSON.parse(data);
                $scope.userhistory=hist;
            });

		}
	};

}]);


