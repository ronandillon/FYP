Quotr.factory('Top20', ['$rootScope',function($scope) {

    //$("#searchText").hide();

	return{

		top20: function(){

			url="http://52.30.239.185/top20";

		    $.get(url, function(data){

                currTop20=JSON.parse(data);
                alert(currTop20[1][1]);

            });

		},
        mtop20: function(){

			url="http://52.30.239.185/mtop20";

		     $.get(url, function(mdata){

                currmTop20=JSON.parse(mdata);
                alert(currmTop20[1][1]);

            });

		},
        stop20: function(){

			url="http://52.30.239.185/stop20";

		    $.get(url, function(sdata){

                currsTop20=JSON.parse(sdata);
                alert(currsTop20[1][1]);

            });

		},
        etop20: function(){

			url="http://52.30.239.185/etop20";

		     $.get(url, function(edata){

                curreTop20=JSON.parse(edata);
                alert(curreTop20[1][1]);

            });

		}
	};

}]);
