Quotr.factory('Top20', ['$rootScope',function($scope) {

    //$("#searchText").hide();

	return{


        top20: function(type){

			url="http://52.30.239.185/"+type;

		     $.get(url, function(data){

                currTop20=JSON.parse(data);
                $scope.list=currTop20;

            });

		}
	};



}]);
