Quotr.factory('History', ['$rootScope',function($scope,$http) {

    //$("#searchText").hide();

	return{

		showhistory: function(uuid){

			$.ajax({
                url: 'http://52.30.239.185/history/\''+uuid+'\'',
                type: 'GET',
                success: function(data){
					if(data=='[]'){
						 $("#noHistory").text("You have no history yet.");
					}
					else {
						hist = JSON.parse(data);
						$scope.userhistory = hist;
					}
				 },
                error: function(data) {
                    $("#noHistory").text("You have no history yet.");
                }
			});

		    /*
		    url="http://52.30.239.185/history/'"+uuid+"'";
		    $.get(url, function(data){
				hist=JSON.parse(data);
                $scope.userhistory=hist;

            })*/

		}
	};

}]);


