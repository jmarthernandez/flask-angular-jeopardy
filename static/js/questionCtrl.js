var app = angular.module('myApp');

app.controller('QuestionController', ['$scope', 'Question', function($scope, Question) {
  $scope.getQuestion = function () {
    Question.retrieve()
      .success(function (question) {
        $scope.question = question[0]
      })
      .error(function (err) {
        console.error(err)
      });
  }

  $scope.getQuestion()
}]);