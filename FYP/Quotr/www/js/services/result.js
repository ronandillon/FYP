Quotr.factory('Result', ['$rootScope','$compile',function($scope,$compile) {

    //$("#searchText").hide();

	return{

		search: function(uuid,toSearch){


            $scope.recommended="";

            $.ajax({
                url: 'http://52.30.239.185/search/'+toSearch+'/'+uuid,
                type: 'GET',
                success: function(data){

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
                    $('#poster').attr("alt",parsed.imdbID);
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


                },
                error: function(data) {
                    location.href = "#/noresult";

                    $("#quoteSearched").text(toSearch);

                }
            });



		    /*
		    url="http://52.30.239.185/search/"+toSearch+"/"+uuid;
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
                $('#poster').attr("alt",parsed.imdbID);
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

    	    });*/
            location.href = "#/result";
            $("#quoteText").text("");


		},

        cancel: function(){
            $("#quoteText").text("");
            location.href = "#";

		},

        recommend: function(imdbId,uuid){
            url="http://52.30.239.185/ref/"+imdbId+"/"+uuid;
            $.get(url, function(data){
                rec=JSON.parse(data);
                $scope.recommended=rec;
            });
        }
	};


}]);
