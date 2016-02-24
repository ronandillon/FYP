var Quotr = angular.module('Quotr', ['ngRoute']).constant('FIREBASE_URL');


Quotr.config(['$routeProvider', function($routeProvider) {
  
  $routeProvider.
	when('/home', {
      templateUrl: 'views/home.html',
      controller: 'Controller'
      
    }).
    when('/top20', {
      templateUrl: 'views/top20.html',
      controller: 'Controller'
      
    }).
    when('/history', {
      templateUrl: 'views/history.html',
      controller: 'Controller'
    }).
    when('/about', {
      templateUrl: 'views/about.html',
      controller: 'Controller',
      
    }).
    otherwise({
      redirectTo: '/home'
    });
}]);

Quotr.run(['$rootScope','$location', function($rootScope,$location){
	
	$rootScope.$on('$routeChangeError',function(event,next,previous,error){
		if(error=='AUTH_REQUIRED'){
			$rootScope.message='Sorry, you must log in to access that page';
			$location.path('/home');
		}

	});
}]);