Quotr.factory('Home', ['$rootScope',function($scope) {

    //$("#searchText").hide();

	return{

		record: function(recording){

			if(recording==true){
                //hide nav bar to keep user on the page while recording
                $("#nav").hide();
                var results = 1;
                var promptString = "Speak now";
                window.plugins.speechrecognizer.startRecognize(function(result){
                    alert(result);
                }, function(errorMessage){

                    console.log("Error message: " + errorMessage);
                }, results, promptString, language);
				alert("can i get a well boi");
				
			}
			else{
				
				location.href = "#/search";

			}

		}
	};
  
}]);
  