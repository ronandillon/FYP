Quotr.controller('Controller',['$scope','Home','Result','History','Top20',function($scope,Home,Result,History,Top20) {
  
	var uuid="";

	document.addEventListener("deviceready", onDeviceReady, false);
	function onDeviceReady() {
    	uuid=device.uuid;
	}

	$scope.record = function() {


		Home.record();

	};

	$scope.search= function() {
		//Send to contents of text box to result.js service where user will be brought to result page
		Result.search(uuid);
	};
	$scope.cancel= function() {
		//Cancels search
		Result.cancel();
	};


	$scope.showhistory= function() {
		//Show history of a user

		History.showhistory(uuid);
	};

	$scope.top20= function(type) {
		//Top 20 searched Series and Movies
		Top20.top20(type);
	};


}]);