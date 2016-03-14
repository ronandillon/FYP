Quotr.factory('Home', ['$rootScope',function($scope) {

    //$("#searchText").hide();

	return{

		record: function(recording){
			alert("home");
			if(recording==true){
                //hide nav bar to keep user on the page while recording
                $("#nav").hide();
                alert("start speech to text");
				
			}
			else{
				
				location.href = "#/search";

			}

		}
	};
  
}]);
  