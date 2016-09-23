Quotr.controller('Controller',['$scope','Home','Result','History','Top20',function($scope,Home,Result,History,Top20) {
  
	var uuid="";

	document.addEventListener("deviceready", onDeviceReady, false);
	function onDeviceReady() {
		//collects the users unique ID
    	uuid=device.uuid;
	}

	$scope.record = function() {
		//Creates the dialog box so a user can edit their quote
		bootbox.dialog({
                title: "Edit Your Quote",
                message: '<div class="row"width="100%">  ' +
                    '<div class="col-md-12"width="100%"> ' +
                    '<form class="form-horizontal"> ' +
                    '<div class="form-group" width="100%"> ' +
                    '<div class="col-md-4" width="100%" > ' +
                    '<textarea id="quoteText"  type="text"  style="font-size: 26px;" rows="8"></textarea> ' +
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

		//Records a user's speech to change to text
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

	$scope.retrieve= function(imdbId) {
		//Retrieves show details after a user presses on a top20/history/recommended show
		Result.search(uuid,imdbId);
	};

	$scope.recommend= function() {
		//Collects the details of recommended shows based on the show that is currently being viewed
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








}]);