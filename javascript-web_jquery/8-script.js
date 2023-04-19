#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (data) {
  $.each(data.results, function (key, value) {
    $('UL#list_movies').append('<li>' + value.title + '</li>');
  });
});
