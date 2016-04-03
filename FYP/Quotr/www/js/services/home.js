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


		},

		dialog: function(){
			bootbox.dialog({
                title: "Edit Your Quote",
                message: '<div width="100%">  ' +
                    '<div width="100%"> ' +
                    '<form  width="100%"> ' +
                    '<div > ' +
                    '<div width="100%" > ' +
                    '<textarea id="quoteText"  type="text" width="100%" style="font-size: 26px;" rows="8"></textarea> ' +
                    '<span class="help-block"></span> </div> ' +
                    '</div> ' +
                    '</form> </div> </div>',
                buttons: {
					cancel:{
						label:"Cancel",
						callback: function(){

						}
					},
                    success: {
                        label: "Send",
                        className: "btn-success",
						size: "large",
                        callback: function () {
                            Result.search(uuid,$("#quoteText").val());
                        }
                    }

                }
            }
        );
		}
	};

}]);
