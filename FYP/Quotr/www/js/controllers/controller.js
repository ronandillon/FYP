Quotr.controller('Controller',['$scope','Home',function($scope,Home) {
  
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
		url="http://52.30.239.185/search/"+$("#quoteText").val()+"/"+uuid;


		$.get(url, function(data){

			parsed=JSON.parse(data);
			if(parsed.Type!="Episode")
			{
				$('#seasontab').hide();
				$('#episodetab').hide();
			}
			else
			{
				$('#season').text(parsed.Season);
				$('#episode').text(parsed.Episode);

			}
			$('#plot').text(parsed.Plot);
			$('#poster').attr("src",parsed.Poster);
			$('#rated').text(parsed.Rated);
			$('#title').text(parsed.Title);
			$('#writer').text(parsed.Writer);
			$('#actor').text(parsed.Actors);
			$('#director').text(parsed.Director);
			$('#genre').text(parsed.Genre);
			$('#year').text(parsed.Year);
			$('#runtime').text(parsed.Runtime);
			$('#country').text(parsed.Country);
			$('#language').text(parsed.Language);
			$('#imdbrating').text(parsed.imdbRating);
			$('#released').text(parsed.Released);


    	});

		$("#quoteText").text("");
		location.href = "#/result";





	};
	$scope.cancel= function() {
		//Cancels search

		$("#quoteText").text("");
		location.href = "#";
	};



}]);




