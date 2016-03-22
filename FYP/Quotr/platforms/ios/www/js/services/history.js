Quotr.factory('History', ['$rootScope',function($scope) {

    //$("#searchText").hide();

	return{

		showhistory: function(uuid){

			url="http://52.30.239.185/history/'"+uuid+"'";

            alert(url);
		    $.get(url, function(data){
                alert(data);
            });

		}
	};

}]);
