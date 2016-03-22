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


	$scope.top20= function() {
		//Top 20 searched Series and Movies
		alert("help1");
		Top20.top20();
	};
	$scope.mtop20= function() {
		//Top 20 searched movies
		alert("help2");
		Top20.mtop20();
	};
	$scope.stop20= function() {
		//Top 20 searched series
		alert("help3");
		Top20.stop20();
	};
	$scope.etop20= function() {
		//Top 20 searched episodes
		alert("help4");
		Top20.etop20();
	};
	$scope.scup= function() {
		//Top 20 searched episodes
		alert("scup?");
		document.write("help");
	};


}]);




