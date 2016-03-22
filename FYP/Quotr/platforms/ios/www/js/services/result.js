Quotr.factory('Result', ['$rootScope',function($scope) {

    //$("#searchText").hide();

	return{

		search: function(uuid){

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

		},

        cancel: function(){
            $("#quoteText").text("");
            location.href = "#";

		}
	};

}]);
