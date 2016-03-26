Quotr.factory('Home', ['$rootScope',function($scope) {

    //$("#searchText").hide();

	return{

		record: function(){

			var maxMatches = 1;
			var promptString = "Speak now"; // optional
			var language = "en-US";                     // optional
			window.plugins.speechrecognizer.startRecognize(function(result){
				$("#quoteText").val(result);

			}, function(errorMessage){

				console.log("Error message: " + errorMessage);
			}, maxMatches, promptString, language);
			//location.href = "#/search";

		}
	};

}]);
