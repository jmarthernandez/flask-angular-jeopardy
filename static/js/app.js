'use strict';

// Declare app level module which depends on views, and components
var app = angular.module('myApp', ['ngMaterial']);

app.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}]);