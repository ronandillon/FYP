Quotr.controller('Controller',['$scope','Home',function($scope,Home) {
  
	var record=false;
  
	$scope.search = function() {
	  
		if(record==false){
			record=true;
		}
		else{
			record=false;
		}
		Home.search(record);
	};


}]);