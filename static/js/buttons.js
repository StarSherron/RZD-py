// Функционал кнопки ДОСУГ
$(function() {
    $('a#leisurebtn').bind('click', function() {
        $.getJSON('/leisure',
            function(data) {
          });
      return false;
    });
})

// Функционал кнопки ЗАРЯДКА
$(function() {
    $('a#chargebtn').bind('click', function() {
        $.getJSON('/charge',
            function(data) {
          });
      return false;
    });
})

// Функционал кнопки БАГАЖ
$(function() {
    $('a#baggagebtn').bind('click', function() {
        $.getJSON('/baggage',
            function(data) {
          });
      return false;
    });
})

// Функционал кнопки НАВИГАЦИЯ
$(function() {
    $('a#navigationbtn').bind('click', function() {
        $.getJSON('/navigation',
            function(data) {
          });
      return false;
    });
})