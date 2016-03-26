Quotr.controller('Controller',['$scope','Home','Result','History','Top20',function($scope,Home,Result,History,Top20) {
  
	var uuid="";

	document.addEventListener("deviceready", onDeviceReady, false);
	function onDeviceReady() {
    	uuid=device.uuid;
	}

	$scope.record = function() {



		bootbox.dialog({
                title: "Edit Your Quote",
                message: '<div class="row"width="100%">  ' +
                    '<div class="col-md-12"width="100%"> ' +
                    '<form class="form-horizontal"> ' +
                    '<div class="form-group" width="100%"> ' +
                    '<div class="col-md-4" width="100%" > ' +
                    '<textarea id="quoteText"  type="text" width="300px" style="font-size: 50px;" rows="12"></textarea> ' +
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

		Home.record();

	};

	$scope.search= function() {
		//Send to contents of text box to result.js service where user will be brought to result page
		Result.search(uuid,$("#quoteText").val());
	};
	$scope.cancel= function() {
		//Cancels search
		Result.cancel();
	};


	$scope.recommend= function() {

		Result.recommend($('#poster').attr('alt'),uuid);
	};

	$scope.showhistory= function() {
		//Show history of a user

		History.showhistory(uuid);
	};

	$scope.top20= function(type) {
		//Top 20 searched Series and Movies
		Top20.top20(type);
	};

	$scope.retrieve= function(imdbId) {
		Result.search(uuid,imdbId);
	};




}]);