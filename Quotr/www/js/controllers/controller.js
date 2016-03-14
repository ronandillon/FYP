Quotr.controller('Controller',['$scope','Home',function($scope,Home) {
  
	var recording=false;


	$scope.record = function() {

		if(recording==false){
			recording=true;

		}
		else{
			recording=false;


		}
		Home.record(recording);

	};
	$scope.search= function() {
		//Send to contents of text box to result.js service where user will be brought to result page

		$("#nav").show();
		$("#tagButton").show();
		url="http://52.30.239.185/search/"+$("#quoteText").val()+"/1";
		$.get(url, function(data){



			parsed=JSON.parse(data);

			if(parsed.Type!="Episode")
			{
				$('#seasontab').hide();
				$('#episodetab').hide();
			}
			$('#plot').text(parsed.Plot);
			$('#poster').attr("src",parsed.Poster);
			$('#rated').text(parsed.Rated);
			$('#title').text(parsed.Title);
			$('#writer').text(parsed.Writer);
			$('#actor').text(parsed.Actors);
			$('#season').text(parsed.Season);
			$('#episode').text(parsed.Episode);
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
		$("#nav").show();
		$("#tagButton").show();
		$("#quoteText").text("");
		location.href = "#";
	};

}]);




