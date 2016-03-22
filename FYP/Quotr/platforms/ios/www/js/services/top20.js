Quotr.factory('Top20', ['$rootScope',function($scope) {

    //$("#searchText").hide();

	return{

		top20: function(){

			url="http://52.30.239.185/top20";

		    $.get(url, function(data){

                currTop20=JSON.parse(data);
                displayTop(currTop20);
            });

		},
        mtop20: function(){

			url="http://52.30.239.185/mtop20";

		     $.get(url, function(mdata){

                currmTop20=JSON.parse(mdata);
                displayTop(currmTop20);

            });

		},
        stop20: function(){

			url="http://52.30.239.185/stop20";

		    $.get(url, function(sdata){

                currsTop20=JSON.parse(sdata);
                displayTop(currsTop20);

            });

		},
        etop20: function(){

			url="http://52.30.239.185/etop20";

		     $.get(url, function(edata){

                curreTop20=JSON.parse(edata);
                displayTop(curreTop20);

            });

		}
	};

    function displayTop(list){
        alert(list[0]);

    };

}]);
