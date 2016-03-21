Quotr.controller('Controller',['$scope','Home','Result',function($scope,Home,Result) {
  
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
		Result.search();
	};
	$scope.cancel= function() {
		//Cancels search
		Result.cancel();
	};



}]);




