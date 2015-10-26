angular.module('myApp')
  .factory("Question", function( $http ) {
    return({
        retrieve: retrieve,
    });

    function retrieve () {
      return $http({
        method  : 'GET',
        url     : '/api/question',
      })
    };

  });
